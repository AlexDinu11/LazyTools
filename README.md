# LazyTools
![Version](https://img.shields.io/badge/version-v0.1.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-yellow)

> **Built out of laziness.**
> *If I have to solve the same problem twice, it probably belongs here.*

LazyTools is my personal collection of lightweight Python utilities built to automate repetitive tasks and simplify development. Every module exists because I got tired of solving the same problem over and over again.

The goal is simple: create reusable utilities that can be dropped into almost any Python project.

---

# Modules

## Colors

Utilities for working with RGB and hexadecimal colors.

### Features

* RGB ↔ HEX conversion
* Blend two colors
* Generate smooth color gradients
* Lighten or darken colors
* Accepts:

  * HEX strings (`"#00bf35"` or `"00bf35"`)
  * RGB lists (`[0, 191, 53]`)
  * RGB tuples (`(0, 191, 53)`)

### Example

```python
from lazytools import colors

print(colors.convert("#00bf35", "rgb"))
print(colors.convert([0, 191, 53], "hex"))

print(colors.blend("#ff0000", "#0000ff", 0.5))

print(colors.gradient("#123456", "#abcdef", 5))
```

### Larger Example

```python
gradient = colors.gradient("#ff0000", "#0000ff", 256)
```

The gradient below was generated using `colors.gradient()` and rendered with Pillow.

![Gradient Preview](examples/gradient.png)

> **Note:** RGB uses 8-bit color channels (0–255). Extremely large gradients may contain repeated colors because there are only 256 unique values available per channel.

---

## CTk Recoloring *(Work in Progress)*

Utilities for recoloring CustomTkinter assets and themes.

This module is still being generalized before its first public release.

---

## Debug *(Coming Later)*

A small collection of debugging utilities used throughout my own projects.

---

# Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/LazyTools.git
```

or download it as a ZIP and copy the `lazytools` folder into your project.

Example project structure:

```text
my_project/
│
├── main.py
└── lazytools/
    ├── __init__.py
    ├── colors.py
    └── ...
```

Import a module:

```python
from lazytools import colors
```

---

# Philosophy

LazyTools is **not** intended to become a large framework.

Instead, it's a growing collection of utilities that solve small, annoying problems. If I find myself rewriting the same code or repeating the same task often enough, it has a good chance of ending up here.

---

# Roadmap

* [x] Color conversion
* [x] Color blending
* [x] Color gradients
* [x] Color manipulation
* [ ] Improve CTk recoloring
* [ ] Add debugging utilities
* [ ] Publish on PyPI

---

# Contributing

Suggestions, bug reports, and improvements are always welcome.

---

# License

This project is licensed under the MIT License.
