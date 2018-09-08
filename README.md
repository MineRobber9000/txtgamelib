# txtgamelib

A library for text games.

## Goals

 - [X] Resource loaders
 - [ ] Menu system
    - [ ] Curses wrapper
        - [X] Crashes don't mess up the screen
	- [ ] Abstract away curses lib
            - [ ] Use urwid instead?

## Resources (`txtgamelib.resource`)

 - `ResourceLoader` - Resolves asset names (see below).
 - `Resource` - Allows for R/W of assets by asset name (see below).

### Asset names

Asset names follow 2 formats:

 - Namespaced: `namespace:path/to/asset.ext`, resolves to `assets/namespace/path/to/asset.ext`.
 - Non-namespaced: `path/to/asset.txt`, resolves to `assets/path/to/asset.ext`.

## Resolver (`txtgamelib.resolver`)

Allows for resolving names to objects. Use `txtgamelib.resolver.Resolver.addResolver` to add functions to resolve names.

`txtgamelib.resource.ResourceLoader` is an example of a `Resolver`.

## Menu (`txtgamelib.menu`)

The `txtgamelib.menu.Menu` screen is a Curses GUI handler. Subclass it and change the draw_menu function. Curses tutorial can be found [here](https://docs.python.org/3/howto/curses.html).
