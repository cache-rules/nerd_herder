import React, { Component } from 'react';
import { Form, Input } from './Form';

const TALK_TYPE_CHOICES = [
  { value: '', label: 'Select a type' },
  { value: 'lightning', label: 'Lightning (5-10 minutes)' },
  { value: 'full_length', label: 'Full Length (~25 minutes)' },
];

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


class TalkForm extends Component {
  constructor(props) {
    super(props);
    const { talk = defaultTalk } = props;

    this.save = this.save.bind(this);
    this.updateValue = this.updateValue.bind(this);
    this.state = {
      talk: {...talk},
      errors: {...defaultErrors},
    };
  }

  validate() {
    const { name, email, title, description, talkType } = this.state.talk;
    let valid = true;

    const errors = Object.keys(defaultErrors).reduce((errors, field) => {
      const value = this.state.talk[field].trim();

      if (value === '') {
        valid = false;
        errors[field] = 'Required';
      }

      return errors;
    }, {...defaultErrors});

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

  save() {
    let talk = null;
    let errors = {...defaultErrors};

    try {
      talk = this.validate();
    } catch (e) {
      errors = e;
    }

    this.setState(() => ({ errors }));

    if (talk !== null) {
      this.props.save(talk);
    }
  }

  updateValue(attr, value) {
    this.setState(state => ({
      talk: {
        ...state.talk,
        [attr]: value,
      },
    }));
  }

  render() {
    const { talk, errors } = this.state;

    return (
      <Form save={this.save} cancel={this.props.cancel}>
        <div className="field">
          <p>All fields are required.</p>
        </div>

        <Input
          required
          type="text"
          label="Name"
          value={talk.name}
          error={errors.name}
          onChange={value => this.updateValue('name', value)}
        />

        <Input
          required
          type="text"
          label="Email"
          value={talk.email}
          error={errors.email}
          onChange={value => this.updateValue('email', value)}
        />

        <Input
          required
          type="text"
          label="Talk title"
          value={talk.title}
          error={errors.title}
          onChange={value => this.updateValue('title', value)}
        />

        <Input
          required
          type="textarea"
          label="Talk description"
          value={talk.description}
          error={errors.description}
          onChange={value => this.updateValue('description', value)}
        />

        <Input
          type="select"
          name="talk_type"
          label="Talk type"
          value={talk.talkType}
          error={errors.talkType}
          options={TALK_TYPE_CHOICES}
          onChange={value => this.updateValue('talkType', value)}
        />
      </Form>
    );
  }
}

export default TalkForm;
