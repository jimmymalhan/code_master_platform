# Rabbit

## Description
This project demonstrates the implementation of memoization for asynchronous functions using TypeScript to optimize performance by caching results of network requests.

## Prerequisites
- Node.js
- npm

## Installation
Clone the repository and install dependencies:
- `git clone <repository-url>`
- `cd rabbit`
- `npm install`

## How to Run
- Start the application: `npm start`
- Build the application for production: `npm run build`
- Run tests to ensure everything is working as expected: `npm test`

## Troubleshooting
If encountering issues:
```bash
npm cache clean --force
rm -rf node_modules dist/
npm install
```

/project-root
├── src/                 # Source files
│   ├── memoizeAsync.ts  # Implementation of memoizeAsync function
│   ├── expensiveFunction.ts # Asynchronous function to be memoized
│   └── index.ts         # Main entry point, possibly for testing implementations
├── tests/               # Test files
│   ├── memoizeAsync.test.ts # Tests for memoizeAsync function
│   └── expensiveFunction.test.ts # Tests for expensiveFunction functionality
├── node_modules/        # Node.js packages (not tracked in git)
├── package.json         # Project metadata and dependencies
├── package-lock.json    # Locked dependency tree
├── jest.config.js       # Jest configuration
├── tsconfig.json        # TypeScript configuration
├── README.md            # Project overview and setup instructions
└── todo.md              # Additional notes or tasks (if applicable)