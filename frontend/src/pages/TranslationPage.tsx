import React, { useState } from 'react';
import { 
  Box, 
  Button, 
  TextField, 
  Typography, 
  Paper,
  FormControl,
  Select,
  MenuItem,
  SelectChangeEvent,
  IconButton,
  Alert,
  Snackbar,
  CircularProgress
} from '@mui/material';
import SwapHorizIcon from '@mui/icons-material/SwapHoriz';
import { useNavigate } from 'react-router-dom';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import { translateText } from '../services/api';

const TranslationPage: React.FC = () => {
  const navigate = useNavigate();
  const [sourceText, setSourceText] = useState('');
  const [translatedText, setTranslatedText] = useState('');
  const [sourceLang, setSourceLang] = useState('ar');
  const [targetLang, setTargetLang] = useState('en');
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  const handleTranslate = async () => {
    try {
      setLoading(true);
      setError(null);
      setTranslatedText('');
      
      console.log('Starting translation...');
      console.log('Source language:', sourceLang);
      console.log('Target language:', targetLang);
      console.log('Text to translate:', sourceText);
      
      const direction = sourceLang === 'ar' ? 'ar2en' : 'en2ar';
      const result = await translateText(sourceText, direction);
      
      console.log('Translation result:', result);
      setTranslatedText(result.translated_text);
    } catch (err: any) {
      console.error('Translation error:', err);
      setError(err?.message || 'Translation failed. Please try again.');
      setTranslatedText('');
    } finally {
      setLoading(false);
    }
  };

  const handleSwapLanguages = () => {
    setSourceLang(targetLang);
    setTargetLang(sourceLang);
    setSourceText(translatedText);
    setTranslatedText(sourceText);
  };

  return (
    <Box sx={{ mt: 4 }}>
      <IconButton 
        onClick={() => navigate('/')} 
        sx={{ mb: 2 }}
        aria-label="back to home"
      >
        <ArrowBackIcon />
      </IconButton>

      <Typography variant="h4" component="h1" gutterBottom>
        Translation
      </Typography>

      <Paper elevation={3} sx={{ p: 3, mb: 3 }}>
        <Box sx={{ display: 'flex', alignItems: 'center', mb: 2 }}>
          <FormControl sx={{ minWidth: 120 }}>
            <Select
              value={sourceLang}
              onChange={(e: SelectChangeEvent) => {
                setSourceLang(e.target.value);
                setTargetLang(e.target.value === 'ar' ? 'en' : 'ar');
              }}
            >
              <MenuItem value="ar">Arabic</MenuItem>
              <MenuItem value="en">English</MenuItem>
            </Select>
          </FormControl>

          <IconButton 
            onClick={handleSwapLanguages}
            sx={{ mx: 2 }}
            aria-label="swap languages"
            disabled={loading}
          >
            <SwapHorizIcon />
          </IconButton>

          <FormControl sx={{ minWidth: 120 }}>
            <Select
              value={targetLang}
              onChange={(e: SelectChangeEvent) => {
                setTargetLang(e.target.value);
                setSourceLang(e.target.value === 'ar' ? 'en' : 'ar');
              }}
            >
              <MenuItem value="en">English</MenuItem>
              <MenuItem value="ar">Arabic</MenuItem>
            </Select>
          </FormControl>
        </Box>

        <TextField
          fullWidth
          multiline
          rows={4}
          value={sourceText}
          onChange={(e) => setSourceText(e.target.value)}
          placeholder="Enter text to translate"
          variant="outlined"
          sx={{ mb: 2 }}
          disabled={loading}
        />

        <Button 
          variant="contained" 
          onClick={handleTranslate}
          disabled={!sourceText || loading}
          fullWidth
          startIcon={loading && <CircularProgress size={20} color="inherit" />}
        >
          {loading ? 'Translating...' : 'Translate'}
        </Button>

        {translatedText && (
          <TextField
            fullWidth
            multiline
            rows={4}
            value={translatedText}
            variant="outlined"
            sx={{ mt: 2 }}
            InputProps={{
              readOnly: true,
            }}
          />
        )}
      </Paper>

      <Snackbar 
        open={!!error} 
        autoHideDuration={6000} 
        onClose={() => setError(null)}
        anchorOrigin={{ vertical: 'bottom', horizontal: 'center' }}
      >
        <Alert 
          onClose={() => setError(null)} 
          severity="error" 
          variant="filled"
          sx={{ width: '100%' }}
        >
          {error}
        </Alert>
      </Snackbar>
    </Box>
  );
};

export default TranslationPage;
