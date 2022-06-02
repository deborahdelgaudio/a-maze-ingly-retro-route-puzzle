# A-maze-ingly Retro Route Puzzle

A small python service that offers an endpoint to solve the puzzle.

## The Problem
Write a program that will output a valid route one could follow to collect all specified items within a map. The map is a json description of set of
rooms with allowed path and contained object.
Exercise starts with an input of:
  - json reppresentation of map
  - starting room
  - list of object to collect

```
Room type allowed fields
  id: Integer
  name: String
  north: Integer //referring to a connected room
  south: Integer //referring to a connected room
  west: Integer //referring to a connected room
  east: Integer //referring to a connected room
  objects: List //of Objects
  
Object type allowed fields
  name: String //Object Name
```

## Usage

The application could be used with Docker, the first step is to build the Docker container running:
```shell
docker build -t ${name} .
```

### Build :package:
```shell
 docker run -v $(pwd):/mnt -p 9090:9090 -w /mnt ${name} ./scripts/build.sh
```

### Tests :test_tube:
```shell
 docker run -v $(pwd):/mnt -p 9090:9090 -w /mnt ${name} ./scripts/tests.sh
```

### Run :gear:
```shell
 docker run -v $(pwd):/mnt -p 9090:9090 -w /mnt ${name} ./scripts/run.sh
```