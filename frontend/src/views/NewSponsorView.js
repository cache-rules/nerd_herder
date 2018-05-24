import React, { Component } from 'react';
import NewSponsorForm from '../components/NewSponsorForm';

class NewSponsorView extends Component {
  render() {
    return (
      <div className="main section">
        <div className="container">
          <header>
            <h1 className="title">Become a Sponsor</h1>
          </header>
        </div>

        <div className="container">
          <div className="columns">
            <div className="column is-half">
              <NewSponsorForm />
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default NewSponsorView;
