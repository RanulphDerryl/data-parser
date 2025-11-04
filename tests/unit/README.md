# Data Parser

A lightweight and efficient tool for parsing and transforming structured data.

## Features

- Supports JSON, CSV, and XML formats
- Configurable parsing rules
- Extensible with custom plugins
- CLI and API interfaces

## Installation

```bash
npm install data-parser
```

## Usage

```javascript
const { Parser } = require('data-parser');

const parser = new Parser({
  format: 'json',
  strictMode: true
});

parser.parse('{"key": "value"}')
  .then(result => console.log(result))
  .catch(error => console.error(error));
```

## Configuration

| Option       | Type    | Default | Description                     |
|--------------|---------|---------|---------------------------------|
| `format`     | string  | 'json'  | Input data format               |
| `strictMode` | boolean | false   | Enable strict parsing rules     |

## License

MIT