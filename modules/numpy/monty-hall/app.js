"use strict";

const doorsRow = document.querySelector("#doors");
const doors = [...document.querySelectorAll(".door")];
const hostCopy = document.querySelector("#host-copy");
const gameTitle = document.querySelector("#game-title");
const resultActions = document.querySelector("#result-actions");
const newGameButton = document.querySelector("#new-game");
const playAgainButton = document.querySelector("#play-again");

const statsElements = {
  stay: {
    rate: document.querySelector("#stay-rate"),
    meter: document.querySelector("#stay-meter"),
    wins: document.querySelector("#stay-wins"),
    games: document.querySelector("#stay-games"),
  },
  switch: {
    rate: document.querySelector("#switch-rate"),
    meter: document.querySelector("#switch-meter"),
    wins: document.querySelector("#switch-wins"),
    games: document.querySelector("#switch-games"),
  },
};

const game = {
  phase: "choosing",
  prizeDoor: 0,
  chosenDoor: null,
  revealedDoor: null,
};

const stats = {
  stay: { games: 0, wins: 0 },
  switch: { games: 0, wins: 0 },
  history: [],
};

function randomDoor() {
  return Math.floor(Math.random() * 3);
}

function setPrizeIcon(doorIndex, icon) {
  doors[doorIndex].querySelector(".door__prize").textContent = icon;
}

function setTag(doorIndex, text) {
  doors[doorIndex].querySelector(".door__tag").textContent = text;
}

function openDoor(doorIndex, contents) {
  setPrizeIcon(doorIndex, contents === "car" ? "🚗" : "🐐");
  doors[doorIndex].classList.add("is-open");
  doors[doorIndex].disabled = true;
  doors[doorIndex].setAttribute(
    "aria-label",
    `Door ${doorIndex + 1}, open, showing a ${contents}`,
  );
}

function otherClosedDoor() {
  return [0, 1, 2].find(
    (door) => door !== game.chosenDoor && door !== game.revealedDoor,
  );
}

function startGame() {
  game.phase = "choosing";
  game.prizeDoor = randomDoor();
  game.chosenDoor = null;
  game.revealedDoor = null;

  gameTitle.textContent = "Choose your first door";
  hostCopy.textContent = "The car is hidden. Which door do you choose?";
  resultActions.hidden = true;
  doorsRow.classList.remove("is-deciding");

  doors.forEach((door, index) => {
    door.disabled = false;
    door.classList.remove("is-selected", "is-open", "is-offer", "is-previous");
    door.setAttribute("aria-label", `Choose door ${index + 1}`);
    setPrizeIcon(index, "");
    setTag(index, "");
  });
}

function chooseDoor(chosenDoor) {
  game.phase = "deciding";
  game.chosenDoor = chosenDoor;

  // Monty knows where the car is and opens a goat door you did not pick.
  const possibleReveals = [0, 1, 2].filter(
    (door) => door !== game.chosenDoor && door !== game.prizeDoor,
  );
  game.revealedDoor = possibleReveals[Math.floor(Math.random() * possibleReveals.length)];
  const offer = otherClosedDoor();

  doors[chosenDoor].classList.add("is-selected");
  setTag(chosenDoor, "Your pick");
  doors[chosenDoor].setAttribute(
    "aria-label",
    `Door ${chosenDoor + 1}, your pick. Click to stay with it`,
  );
  doors[offer].classList.add("is-offer");
  setTag(offer, "Switch?");
  doors[offer].setAttribute("aria-label", `Door ${offer + 1}. Click to switch to it`);

  openDoor(game.revealedDoor, "goat");
  doorsRow.classList.add("is-deciding");

  gameTitle.textContent = "Stay or switch?";
  hostCopy.textContent =
    `Monty opens door ${game.revealedDoor + 1}: a goat! ` +
    `Click door ${chosenDoor + 1} again to stay, or door ${offer + 1} to switch.`;
}

function finishGame(finalDoor) {
  game.phase = "finished";

  const strategy = finalDoor === game.chosenDoor ? "stay" : "switch";
  const won = finalDoor === game.prizeDoor;

  doorsRow.classList.remove("is-deciding");
  doors.forEach((door) => door.classList.remove("is-offer", "is-selected"));
  doors[finalDoor].classList.add("is-selected");
  setTag(finalDoor, "Final pick");
  if (strategy === "switch") {
    doors[game.chosenDoor].classList.add("is-previous");
    setTag(game.chosenDoor, "First pick");
  } else {
    setTag(otherClosedDoor(), "");
  }

  [0, 1, 2]
    .filter((door) => door !== game.revealedDoor)
    .forEach((door) => openDoor(door, door === game.prizeDoor ? "car" : "goat"));

  stats[strategy].games += 1;
  if (won) stats[strategy].wins += 1;
  stats.history.unshift({ strategy, won });
  stats.history = stats.history.slice(0, 12);
  updateStats();

  const action = strategy === "stay" ? "stayed" : "switched";
  gameTitle.textContent = won ? "You won the car!" : "A goat, this time";
  hostCopy.textContent = won
    ? `You ${action} — and won the car!`
    : `You ${action} — but the car was behind door ${game.prizeDoor + 1}.`;
  resultActions.hidden = false;
}

function handleDoorClick(doorIndex) {
  if (game.phase === "choosing") {
    chooseDoor(doorIndex);
  } else if (game.phase === "deciding" && doorIndex !== game.revealedDoor) {
    finishGame(doorIndex);
  }
}

function updateStats() {
  ["stay", "switch"].forEach((strategy) => {
    const { games, wins } = stats[strategy];
    const rate = games === 0 ? 0 : (wins / games) * 100;
    statsElements[strategy].rate.textContent = games === 0 ? "—" : `${Math.round(rate)}%`;
    statsElements[strategy].meter.style.width = `${rate}%`;
    statsElements[strategy].wins.textContent = wins;
    statsElements[strategy].games.textContent = games;
  });

  const history = document.querySelector("#history");
  if (stats.history.length === 0) {
    history.innerHTML = '<span class="history__empty">Play a round to begin collecting evidence.</span>';
    return;
  }

  history.replaceChildren(
    ...stats.history.map(({ strategy, won }) => {
      const item = document.createElement("span");
      item.className = `history__item${won ? "" : " is-loss"}`;
      item.textContent = `${strategy === "stay" ? "Stayed" : "Switched"} · ${won ? "won" : "lost"}`;
      return item;
    }),
  );
}

function resetStats() {
  stats.stay = { games: 0, wins: 0 };
  stats.switch = { games: 0, wins: 0 };
  stats.history = [];
  updateStats();
}

function simulate(rounds) {
  let stayWins = 0;
  let switchWins = 0;

  for (let round = 0; round < rounds; round += 1) {
    const prize = randomDoor();
    const firstPick = randomDoor();
    if (prize === firstPick) {
      stayWins += 1;
    } else {
      switchWins += 1;
    }
  }

  const stayRate = (stayWins / rounds) * 100;
  const switchRate = (switchWins / rounds) * 100;

  document.querySelector("#simulation-count").textContent = `${rounds.toLocaleString()} simulated games`;
  document.querySelector("#sim-stay-rate").textContent = `${stayRate.toFixed(1)}%`;
  document.querySelector("#sim-switch-rate").textContent = `${switchRate.toFixed(1)}%`;
  document.querySelector("#sim-stay-bar").style.width = `${stayRate}%`;
  document.querySelector("#sim-switch-bar").style.width = `${switchRate}%`;
  document.querySelector("#simulation-note").textContent =
    rounds < 100
      ? "Run it again: small samples naturally bounce around."
      : "As the sample grows, the rates tend to settle near ⅓ and ⅔.";
}

doors.forEach((door) => {
  door.addEventListener("click", () => handleDoorClick(Number(door.dataset.door)));
});

newGameButton.addEventListener("click", startGame);
playAgainButton.addEventListener("click", startGame);
document.querySelector("#reset-stats").addEventListener("click", resetStats);

document.querySelectorAll("[data-simulations]").forEach((button) => {
  button.addEventListener("click", () => simulate(Number(button.dataset.simulations)));
});

const explanationToggle = document.querySelector("#explanation-toggle");
const explanationBody = document.querySelector("#explanation-body");
explanationToggle.addEventListener("click", () => {
  const expanded = explanationToggle.getAttribute("aria-expanded") === "true";
  explanationToggle.setAttribute("aria-expanded", String(!expanded));
  explanationBody.hidden = expanded;
});

startGame();
