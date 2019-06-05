import React, { PureComponent } from 'react';

class TalkSubmittedView extends PureComponent {
  render() {
    return (
      <section className="main section">
        <div className="container">
          <div className="columns">
            <div className="column is-half">
              <h1 className="title">Thank You!</h1>
              <p>Thank you for submitting a talk.</p>
            </div>
          </div>
        </div>
      </section>
    );
  }
}

export default TalkSubmittedView;
