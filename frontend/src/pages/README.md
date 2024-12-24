# Pages Documentation

This directory contains the main page components of the application.

## Components

### HomePage (`HomePage.tsx`)
The landing page of the application featuring:
- Title and description
- Two main cards:
  1. Translation Service Card
  2. Summarization Service Card
- Navigation buttons to respective services
- Material-UI components for consistent styling

#### Usage
```typescript
import HomePage from './pages/HomePage';

// In your router
<Route path="/" element={<HomePage />} />
```

### TranslationPage (`TranslationPage.tsx`)
The translation interface featuring:
- Input text area
- Language direction selector (Arabic ↔ English)
- Translation button
- Output display area
- Error handling and loading states

#### Usage
```typescript
import TranslationPage from './pages/TranslationPage';

// In your router
<Route path="/translate" element={<TranslationPage />} />
```

### SummaryPage (`SummaryPage.tsx`)
The text summarization interface featuring:
- Input text area for long text
- Summarize button
- Summary output display
- Error handling and loading states

#### Usage
```typescript
import SummaryPage from './pages/SummaryPage';

// In your router
<Route path="/summarize" element={<SummaryPage />} />
```

## Styling

All pages use Material-UI components and follow these style guidelines:
- Responsive design for all screen sizes
- Consistent spacing using MUI's spacing system
- Error states with clear user feedback
- Loading indicators for async operations

## Navigation

Navigation between pages is handled using React Router:
- Home: `/`
- Translation: `/translate`
- Summarization: `/summarize`

## Error Handling

Each page includes:
- Input validation
- API error handling
- Loading states
- User feedback for errors
- Retry mechanisms for failed operations
