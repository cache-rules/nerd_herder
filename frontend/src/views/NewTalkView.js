import React, { Component } from 'react';
import { post } from '../api/http';
import TalkForm from '../components/TalkForm';
import { withAudienceChoices } from '../api/AudienceChoice';

function trimToNull(value) {
  const trimmedValue = value.trim();

  if (trimmedValue === '') {
    return null;
  }

  return trimmedValue;
}

function noop() {
  return null;
}

function required(value) {
  if (value === null || value.trim() === '') {
      return 'This field is required.';
  }

  return null;
}

const defaultTalk = {
  email: '',
  name: '',
  title: '',
  description: '',
  talkType: '',
  audience: '',
};

const defaultErrors = {
  name: null,
  email: null,
  title: null,
  description: null,
  talkType: null,
  audience: null,
};

const validators = {
  name: required,
  email: required,
  title: required,
  description: required,
  talkType: required,
  audience: noop,
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
    const { name, email, title, description, talkType, audience } = this.state.talk;
    let valid = true;

    const errors = Object.keys(defaultErrors).reduce(
      (errors, field) => {
        const value = this.state.talk[field];
        const error = validators[field](value);

        if (error !== null) {
          valid = false;
          errors[field] = error;
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
      audience: trimToNull(audience),
    };
  }

  async save(talk) {
    this.setState({ saving: true, saveErrors: {} });
    const response = await post('/api/v1/talk-proposals/', talk);
    this.setState({ saving: false });
    let body;

    try {
      body = await response.json();
    } catch (e) {
      body = {
        other: ['Unexpected error returned from server. Please try again later.'],
      };
    }

    if (response.status >= 400) {
      console.log(body);
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

      this.props.history.push('/speak/success');
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
                audienceChoices={this.props.audienceChoices}
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

export default withAudienceChoices(NewTalkView);
