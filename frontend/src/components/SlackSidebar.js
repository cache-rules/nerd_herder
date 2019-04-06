import React, { Component } from 'react';
import styles from '../SlackSidebar.css';

class SlackSidebar extends Component {
  render() {
    return (
      <section className="SlackSidebar">
        <p>Want to join the PuPPy Slack?</p>
        <a href="http://slack.pspython.com">
          <img src={require('../assets/slack_logo.png')} />
        </a>
      </section>
    );
  }
}

export default SlackSidebar;
