import React, { PureComponent } from 'react';
import { Form, Input } from './Form';

const TALK_TYPE_CHOICES = [
  { value: '', label: 'Select a type' },
  { value: 'lightning', label: 'Lightning (5-10 minutes)' },
  { value: 'full_length', label: 'Full Length (~25 minutes)' },
];

class TalkForm extends PureComponent {
  render() {
    const { saving, talk, errors, updateValue, save, cancel } = this.props;
    const other = errors.other ? errors.other : '';

    return (
      <Form saving={saving} save={save} cancel={cancel}>
        <div className="field">
          <p>All fields are required.</p>

          <p className="has-text-danger">{other}</p>
        </div>

        <Input
          type="text"
          name="name"
          label="Name"
          value={talk.name}
          error={errors.name}
          onChange={updateValue}
        />

        <Input
          type="text"
          name="email"
          label="Email"
          value={talk.email}
          error={errors.email}
          onChange={updateValue}
        />

        <Input
          type="text"
          name="title"
          label="Talk title"
          value={talk.title}
          error={errors.title}
          onChange={updateValue}
        />

        <Input
          type="textarea"
          name="description"
          label="Talk description"
          value={talk.description}
          error={errors.description}
          onChange={updateValue}
        />

        <Input
          type="select"
          name="talkType"
          label="Talk type"
          value={talk.talkType}
          error={errors.talkType}
          options={TALK_TYPE_CHOICES}
          onChange={updateValue}
        />
      </Form>
    );
  }
}

export default TalkForm;
