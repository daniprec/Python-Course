# Computer Programming I (Python)

An introductory Python course designed specifically for Math students.

## 🌐 Website

Visit the course website: [https://daniprec.github.io/Python-Course](https://daniprec.github.io/Python-Course)

## 📚 Course Overview

This course provides a comprehensive introduction to programming using Python. Students will learn fundamental programming concepts and develop practical coding skills through hands-on exercises and projects.

### Modules

1. **Module 1: Introduction to Python** - Learn the fundamentals of Python programming
2. **Module 2: Data Structures** - Explore Python's built-in data structures
3. **Module 3: Control Flow and Functions** - Master conditional statements, loops, and functions
4. **Module 4: Advanced Topics** - Dive into file I/O, error handling, and libraries

## 🚀 Local Development

### Prerequisites

- [Quarto](https://quarto.org/docs/get-started/) (version 1.4 or later)

### Building the Website

```bash
# Clone the repository
git clone https://github.com/daniprec/Python-Course.git
cd Python-Course

# Preview the website locally
quarto preview

# Render the website
quarto render
```

The rendered website will be in the `_site` directory.

## 📖 GitHub Pages Deployment

This website is automatically deployed to GitHub Pages using GitHub Actions.

### Setup Instructions

1. **Enable GitHub Pages**:
   - Go to your repository Settings → Pages
   - Under "Build and deployment", select "GitHub Actions" as the source

2. **Push to Main Branch**:
   - The workflow will automatically run when you push to the `main` branch
   - You can also manually trigger it from the Actions tab

3. **View Your Site**:
   - Once deployed, your site will be available at: `https://yourusername.github.io/Python-Course`

### Manual Deployment

If you prefer to deploy manually:

```bash
# Render the website
quarto render

# Publish to GitHub Pages
quarto publish gh-pages
```

## 📝 Content Structure

```
Python-Course/
├── _quarto.yml          # Quarto configuration
├── index.qmd            # Home page
├── syllabus.qmd         # Course syllabus
├── assets/
│   └── styles.css       # Custom CSS
└── modules/
    ├── module1/         # Introduction to Python
    ├── module2/         # Data Structures
    ├── module3/         # Control Flow and Functions
    └── module4/         # Advanced Topics
```

## ✨ Features

- **Interactive Content**: All code examples with syntax highlighting
- **Collapsible Exercises**: Practice problems with solutions
- **Responsive Design**: Works on desktop and mobile devices
- **Search Functionality**: Built-in search across all content
- **Dark Mode Support**: Automatic theme switching

## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/daniprec/Python-Course/issues).

## 👨‍💻 Author

**daniprec**

- GitHub: [@daniprec](https://github.com/daniprec)

## 🙏 Acknowledgments

- Built with [Quarto](https://quarto.org/)
- Designed for Math students learning Python programming
