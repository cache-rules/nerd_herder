import React, { Component } from 'react';
import { post } from '../api/http';
import TalkForm from '../components/TalkForm';

const defaultTalk = {
  email: '',
  name: '',
  title: '',
  description: '',
  talkType: '',
};

const defaultErrors = {
  name: null,
  email: null,
  title: null,
  description: null,
  talkType: null,
};

class NewTalkView extends Component {
  constructor(props) {
    super(props);
    this.updateTalkValue = this.updateTalkValue.bind(this);
    this.validate = this.validate.bind(this);
    this.save = this.save.bind(this);
    this.onSave = this.onSave.bind(this);
    this.onCancel = this.onCancel.bind(this);

    this.state = {
      saving: false,
      saveErrors: {},
      talk: { ...defaultTalk },
      errors: { ...defaultErrors },
    };
  }

  updateTalkValue(value) {
    // value is an object that looks like { attributeName: value }
    // Example: { name: 'Alan Vezina' }
    this.setState(state => ({
      talk: {
        ...state.talk,
        ...value,
      },
    }));
  }

  validate() {
    const { name, email, title, description, talkType } = this.state.talk;
    let valid = true;

    const errors = Object.keys(defaultErrors).reduce(
      (errors, field) => {
        const value = this.state.talk[field].trim();

        if (value === '') {
          valid = false;
          errors[field] = 'This field is required.';
        }

        return errors;
      },
      { ...defaultErrors }
    );

    if (valid === false) {
      throw errors;
    }

    return {
      name,
      email,
      title,
      description,
      talk_type: talkType,
    };
  }

  async save(talk) {
    this.setState({ saving: true, saveErrors: {} });
    const response = await post('/api/talks', talk);
    this.setState({ saving: false });
    const body = await response.json();

    if (response.status >= 400) {
      const errors = Object.keys(body).reduce(
        (errors, attr) => {
          errors[attr] = body[attr].join(' ');
          return errors;
        },
        { ...defaultErrors }
      );

      this.setState(() => ({ errors }));
    } else {
      this.setState(() => ({
        errors: {
          ...defaultErrors,
        },
      }));
    }
  }

  onSave() {
    let talk = null;
    let errors = { ...defaultErrors };

    try {
      talk = this.validate();
    } catch (e) {
      errors = e;
    }

    this.setState(() => ({ errors }));

    if (talk !== null) {
      this.save(talk);
    }
  }

  onCancel() {
    this.props.history.push('/');
  }

  render() {
    return (
      <section className="main section">
        <div className="container">
          <h1 className="title">Submit a Talk</h1>
        </div>

        <div className="container">
          <div className="columns">
            <div className="column is-half">
              <TalkForm
                saving={this.state.saving}
                talk={this.state.talk}
                errors={this.state.errors}
                updateValue={this.updateTalkValue}
                save={this.onSave}
                cancel={this.onCancel}
              />
            </div>
          </div>
        </div>
      </section>
    );
  }
}

export default NewTalkView;
