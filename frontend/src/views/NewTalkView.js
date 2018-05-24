import React, { Component } from 'react';
import { post } from '../api/http';
import TalkForm from '../components/TalkForm';

class NewTalkView extends Component {
  constructor(props) {
    super(props);
    this.save = this.save.bind(this);

    this.state = {
      saving: false,
      saveErrors: {},
    };
  }

  async save(talk) {
    console.log('Save new talk!', talk);
    this.setState({ saving: true });
    await post('/api/talks', talk);
  }

  render() {
    return (
      <section className="main section">
        <div className="container">
          <h1 className="title">
            Submit a Talk
          </h1>
        </div>

        <div className="container">
          <div className="columns">
            <div className="column is-half">
              <TalkForm
                saving={this.state.saving}
                saveErrors={this.state.saveErrors}
                save={this.save}
              />
            </div>
          </div>
        </div>
      </section>
    );
  }
}

export default NewTalkView;
