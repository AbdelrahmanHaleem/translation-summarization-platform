import React, { useState } from 'react';
import { 
  Box, 
  Button, 
  TextField, 
  Typography, 
  Paper,
  IconButton,
  Alert,
  Snackbar
} from '@mui/material';
import { useNavigate } from 'react-router-dom';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import { summarizeText } from '../services/api';

const SummaryPage: React.FC = () => {
  const navigate = useNavigate();
  const [sourceText, setSourceText] = useState('');
  const [summary, setSummary] = useState('');
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  const handleSummarize = async () => {
    try {
      setLoading(true);
      setError(null);
      const result = await summarizeText(sourceText);
      setSummary(result.summary);
    } catch (err) {
      setError('Summarization failed. Please try again.');
      console.error('Summarization error:', err);
    } finally {
      setLoading(false);
    }
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
        Text Summarization
      </Typography>

      <Paper elevation={3} sx={{ p: 3, mb: 3 }}>
        <TextField
          fullWidth
          multiline
          rows={6}
          value={sourceText}
          onChange={(e) => setSourceText(e.target.value)}
          placeholder="Enter text to summarize"
          variant="outlined"
          sx={{ mb: 2 }}
        />

        <Button 
          variant="contained" 
          onClick={handleSummarize}
          disabled={!sourceText || loading}
          fullWidth
        >
          {loading ? 'Summarizing...' : 'Summarize'}
        </Button>

        {summary && (
          <TextField
            fullWidth
            multiline
            rows={4}
            value={summary}
            variant="outlined"
            sx={{ mt: 2 }}
            InputProps={{
              readOnly: true,
            }}
            label="Summary"
          />
        )}
      </Paper>

      <Snackbar 
        open={!!error} 
        autoHideDuration={6000} 
        onClose={() => setError(null)}
      >
        <Alert onClose={() => setError(null)} severity="error">
          {error}
        </Alert>
      </Snackbar>
    </Box>
  );
};

export default SummaryPage;
