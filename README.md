# txtgamelib

A library for text games.

## Resources (`txtgamelib.resource`)

 - `ResourceLoader` - Resolves asset names (see below).
 - `Resource` - Allows for R/W of assets by asset name (see below).

### Asset names

Asset names follow 2 formats:

 - Namespaced: `namespace:path/to/asset.ext`, resolves to `assets/namespace/ext/path/to/asset.ext`.
 - Non-namespaced: `path/to/asset.txt`, resolves to `assets/ext/path/to/asset.ext`.

## Resolver (`txtgamelib.res`)

Allows for resolving names to objects. Use `txtgamelib.res.Resolver.addResolver` to add functions to resolve names.
