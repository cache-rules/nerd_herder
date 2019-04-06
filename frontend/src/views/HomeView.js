import React, { PureComponent } from 'react';
import { Link } from 'react-router-dom';
import SlackSidebar from '../components/SlackSidebar';

import './HomeView.css';

class HomeView extends PureComponent {
  render() {
    return (
      <section className="home-gradient hero is-fullheight">
        <div className="hero-body">
          <div className="container has-text-centered">
            <div className="level">
              <div className="level-item has-text-centered">
                <a href="https://www.meetup.com/PSPPython/">
                  <div className="home-link-item">
                    <i className="fab fa-meetup fa-4x" />
                    <span className="home-link-item__label">Upcoming events</span>
                  </div>
                </a>
              </div>

              <div className="level-item has-text-centered">
                <div className="vertical-line" />
              </div>

              <div className="level-item has-text-centered">
                <Link to="/speak">
                  <div className="home-link-item">
                    <i className="fas fa-bullhorn fa-4x" />
                    <span className="home-link-item__label">Submit a talk</span>
                  </div>
                </Link>
              </div>

              <div className="level-item has-text-centered">
                <div className="vertical-line" />
              </div>

              <div className="level-item has-text-centered">
                <a href="/pages/code-of-conduct">
                  <div className="home-link-item">
                    <i className="fas fa-file-alt fa-4x" />
                    <span className="home-link-item__label">Code of Conduct</span>
                  </div>
                </a>
              </div>
            </div>
          </div>
        </div>

        <SlackSidebar />

        <div className="hero-foot">
          <div className="container has-text-right">
            <div className="powered-by">
              <span className="fab fa-github" />
              &nbsp; Powered by&nbsp;
              <a href="https://github.com/cache-rules/nerd_herder">nerd_herder</a>
            </div>
          </div>
        </div>
      </section>
    );
  }
}

export default HomeView;
