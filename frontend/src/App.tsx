import React from 'react';
import { Routes, Route } from 'react-router-dom';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import Box from '@mui/material/Box';
import Container from '@mui/material/Container';

// Import pages
import TranslationPage from './pages/TranslationPage';
import SummaryPage from './pages/SummaryPage';
import HomePage from './pages/HomePage';

const theme = createTheme({
  palette: {
    mode: 'light',
    primary: {
      main: '#1976d2',
    },
    secondary: {
      main: '#dc004e',
    },
  },
});

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Box sx={{ flexGrow: 1 }}>
        <Container maxWidth="lg">
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/translate" element={<TranslationPage />} />
            <Route path="/summarize" element={<SummaryPage />} />
          </Routes>
        </Container>
      </Box>
    </ThemeProvider>
  );
}

export default App;
