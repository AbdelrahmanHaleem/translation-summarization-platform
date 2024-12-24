const API_BASE_URL = 'http://localhost:8000';

const checkServerConnection = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/health`, {
      method: 'GET',
    });
    return response.ok;
  } catch (error) {
    console.error('Server connection error:', error);
    return false;
  }
};

export const translateText = async (text: string, direction: 'ar2en' | 'en2ar') => {
  try {
    console.log(`Sending translation request to ${API_BASE_URL}/translate/${direction}`);
    console.log('Request payload:', { text });
    
    // Check server connection first
    const isServerConnected = await checkServerConnection();
    if (!isServerConnected) {
      throw new Error('Cannot connect to translation server. Please make sure the server is running.');
    }
    
    const response = await fetch(`${API_BASE_URL}/translate/${direction}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      },
      body: JSON.stringify({ text }),
      // Add timeout
      signal: AbortSignal.timeout(30000) // 30 second timeout for model loading
    });
    
    console.log('Response status:', response.status);
    const responseData = await response.json();
    console.log('Response data:', responseData);
    
    if (!response.ok) {
      throw new Error(responseData.error || `HTTP error! status: ${response.status}`);
    }
    
    return responseData;
  } catch (error: any) {
    console.error('Translation error:', error);
    if (error.name === 'AbortError') {
      throw new Error('Translation request timed out. Please try again.');
    }
    if (error.message === 'Failed to fetch') {
      throw new Error('Cannot connect to translation server. Please make sure the server is running.');
    }
    throw error;
  }
};

export const summarizeText = async (text: string) => {
  try {
    console.log('Sending summarization request');
    console.log('Request payload:', { text });
    
    // Check server connection first
    const isServerConnected = await checkServerConnection();
    if (!isServerConnected) {
      throw new Error('Cannot connect to summarization server. Please make sure the server is running.');
    }
    
    const response = await fetch(`${API_BASE_URL}/summarize`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      },
      body: JSON.stringify({ text }),
      // Add timeout
      signal: AbortSignal.timeout(30000) // 30 second timeout for model loading
    });
    
    console.log('Response status:', response.status);
    const responseData = await response.json();
    console.log('Response data:', responseData);
    
    if (!response.ok) {
      throw new Error(responseData.error || `HTTP error! status: ${response.status}`);
    }
    
    return responseData;
  } catch (error: any) {
    console.error('Summarization error:', error);
    if (error.name === 'AbortError') {
      throw new Error('Summarization request timed out. Please try again.');
    }
    if (error.message === 'Failed to fetch') {
      throw new Error('Cannot connect to summarization server. Please make sure the server is running.');
    }
    throw error;
  }
};
