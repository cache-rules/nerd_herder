import React, { Component } from 'react';
import { BrowserRouter, Route } from 'react-router-dom';
import HomeView from './views/HomeView';
import NewTalkView from './views/NewTalkView';
import TalkSubmittedView from './views/TalkSubmittedView';
import NewSponsorView from './views/NewSponsorView';
import Header from './components/Header';
import './App.css';

class App extends Component {
  render() {
    return (
      <BrowserRouter basename="/app">
        <div>
          <Route path="/" component={Header} />
          <Route exact path="/" component={HomeView} />
          <Route exact path="/speak" component={NewTalkView} />
          <Route exact path="/speak/success" component={TalkSubmittedView} />
          <Route exact path="/sponsor" component={NewSponsorView} />
        </div>
      </BrowserRouter>
    );
  }
}

export default App;
