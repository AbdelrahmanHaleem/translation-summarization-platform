# Translation & Summarization Platform Frontend

The React-based frontend for the Translation and Summarization Platform.

## Tech Stack

- React 18
- TypeScript
- Material-UI
- React Router
- Fetch API

## Project Structure

```
frontend/
├── src/
│   ├── pages/           # Page components
│   │   ├── HomePage.tsx
│   │   ├── TranslationPage.tsx
│   │   └── SummaryPage.tsx
│   ├── services/        # API services
│   │   └── api.ts
│   ├── components/      # Reusable components
│   ├── App.tsx         # Main app component
│   └── index.tsx       # Entry point
├── public/             # Static assets
└── package.json        # Dependencies and scripts
```

## Setup

1. Install dependencies:
```bash
npm install
```

2. Start development server:
```bash
npm start
```

3. Build for production:
```bash
npm run build
```

## Features

- Modern, responsive UI
- Real-time translation
- Text summarization
- Error handling
- Loading states
- Navigation between services

## Components

### App.tsx
- Main application component
- Routing setup
- Theme configuration
- Layout structure

### Pages
- HomePage: Landing page with service cards
- TranslationPage: Translation interface
- SummaryPage: Summarization interface

### Services
- api.ts: Backend communication
- Error handling
- Request/response types

## Styling

- Material-UI components
- Responsive design
- Custom theme
- Consistent spacing
- Loading animations

## Development

### Available Scripts
- `npm start`: Start development server
- `npm test`: Run tests
- `npm run build`: Build for production
- `npm run eject`: Eject from create-react-app

### Environment
- Development server: http://localhost:3000
- Backend API: http://localhost:8000

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
