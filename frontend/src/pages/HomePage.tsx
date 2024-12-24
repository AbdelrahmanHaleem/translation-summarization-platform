import React from 'react';
import { useNavigate } from 'react-router-dom';
import { Box, Button, Typography, Grid, Paper } from '@mui/material';
import TranslateIcon from '@mui/icons-material/Translate';
import SummarizeIcon from '@mui/icons-material/Summarize';

const HomePage: React.FC = () => {
  const navigate = useNavigate();

  return (
    <Box sx={{ mt: 4 }}>
      <Typography variant="h3" component="h1" gutterBottom align="center">
        Translation & Summarization Platform
      </Typography>
      
      <Grid container spacing={4} sx={{ mt: 4 }}>
        <Grid item xs={12} md={6}>
          <Paper 
            elevation={3} 
            sx={{ 
              p: 3, 
              display: 'flex', 
              flexDirection: 'column', 
              alignItems: 'center',
              minHeight: '200px',
              cursor: 'pointer',
              '&:hover': {
                backgroundColor: 'action.hover'
              }
            }}
            onClick={() => navigate('/translate')}
          >
            <TranslateIcon sx={{ fontSize: 60, mb: 2 }} color="primary" />
            <Typography variant="h5" component="h2" gutterBottom>
              Translation
            </Typography>
            <Typography align="center" color="text.secondary">
              Translate text between Arabic and English
            </Typography>
            <Button 
              variant="contained" 
              sx={{ mt: 2 }}
              startIcon={<TranslateIcon />}
              onClick={() => navigate('/translate')}
            >
              Start Translating
            </Button>
          </Paper>
        </Grid>

        <Grid item xs={12} md={6}>
          <Paper 
            elevation={3} 
            sx={{ 
              p: 3, 
              display: 'flex', 
              flexDirection: 'column', 
              alignItems: 'center',
              minHeight: '200px',
              cursor: 'pointer',
              '&:hover': {
                backgroundColor: 'action.hover'
              }
            }}
            onClick={() => navigate('/summarize')}
          >
            <SummarizeIcon sx={{ fontSize: 60, mb: 2 }} color="primary" />
            <Typography variant="h5" component="h2" gutterBottom>
              Summarization
            </Typography>
            <Typography align="center" color="text.secondary">
              Generate concise summaries of your text
            </Typography>
            <Button 
              variant="contained" 
              sx={{ mt: 2 }}
              startIcon={<SummarizeIcon />}
              onClick={() => navigate('/summarize')}
            >
              Start Summarizing
            </Button>
          </Paper>
        </Grid>
      </Grid>
    </Box>
  );
};

export default HomePage;
