import React from 'react';
import ReactDOM from 'react-dom';
import 'normalize.css';
import './index.css';
import './forms.css';
import App from './App';

if (window.location.pathname === '/') {
  window.location = '/app';
}

ReactDOM.render(<App />, document.getElementById('root'));
