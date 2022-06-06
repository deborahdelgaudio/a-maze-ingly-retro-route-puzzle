# A-maze-ingly Retro Route Puzzle

A small python service that offers an endpoint to solve the puzzle.

## The Problem

Write a program that will output a valid route one could follow to collect all specified items within a map. The map is
a json description of set of
rooms with allowed path and contained object.

Exercise starts with an input of:

- json representation of map
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

## Assumptions

The implementation is based on the following assumptions:
 - A list of objects to collect and a starting room are mandatory parameters.
 - Objects to collect have to be into the map and not empty.
 - The starting room should be an existent room.
 - A valid output path is a path that could be followed and allow the player to pick all the requested objects.
 - The output path is not necessary the shortest.
 - In a room could be more than one object but only requested object are picked.

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

Start the server running:

```shell
 docker run -v $(pwd):/mnt -p 9090:9090 -w /mnt ${name} ./scripts/run.sh
```

At the endpoint: `0.0.0.0:9090/puzzle/find/path` it's possible to play with the application by sending a `POST` request
containing a body like this:

```json
{
  "map": {
    "rooms": [
      {
        "id": 1,
        "name": "Hallway",
        "north": 2,
        "objects": []
      },
      {
        "id": 2,
        "name": "Dining Room",
        "south": 1,
        "west": 3,
        "east": 4,
        "objects": []
      },
      {
        "id": 3,
        "name": "Kitchen",
        "east": 2,
        "objects": [
          {
            "name": "Knife"
          }
        ]
      },
      {
        "id": 4,
        "name": "Sun Room",
        "west": 2,
        "objects": [
          {
            "name": "Potted Plant"
          }
        ]
      }
    ]
  },
  "start_room_id": 2,
  "objects_to_collect": [
    "Knife",
    "Potted Plant"
  ]
}
```
It's also possible to interact with a beautiful interface that contains the entire OpenAPI specification at `0.0.0.0:9090/docs`.

### Repository structure
The implementation follows [The Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html) guidelines.