# Vimboat

A RSS/Atom/Twitter/Manga feed reader in Neovim

# Components 

## Python

- Makes GET-Requests to fetch the feeds
- Parses feed information for the database

## SQLite

- Store the data compatible with newsboat

## Lua

- Configures Neovim to function as a feed selector
- Special highlight groups for feed specific properties

## Neovim

- Offers a more versatile UI than newsboat
- Special mode for viewing and managing feeds and articles

