import React, { PureComponent } from 'react';
import { Form, Input } from './Form';

const TALK_TYPE_CHOICES = [
  { value: '', label: 'Select a type' },
  { value: 'lightning', label: 'Lightning (5 minutes)' },
  { value: 'full_length', label: 'Full Length (~25 minutes)' },
];

class TalkForm extends PureComponent {
  render() {
    const { saving, talk, errors, updateValue, save, cancel, audienceChoices } = this.props;
    const other = errors.other ? errors.other : '';

    return (
      <Form saveText="Submit" saving={saving} save={save} cancel={cancel}>
        <div className="field">
          <p>Fields marked with * are required.</p>

          <p className="has-text-danger">{other}</p>
        </div>

        <Input
          required
          type="text"
          name="name"
          label="Name"
          value={talk.name}
          error={errors.name}
          onChange={updateValue}
        />

        <Input
          required
          type="text"
          name="email"
          label="Email"
          value={talk.email}
          error={errors.email}
          onChange={updateValue}
        />

        <Input
          required
          type="text"
          name="title"
          label="Title"
          value={talk.title}
          error={errors.title}
          onChange={updateValue}
        />

        <Input
          required
          type="textarea"
          name="description"
          label="Description"
          value={talk.description}
          error={errors.description}
          onChange={updateValue}
        />

        <Input
          required
          type="select"
          name="talkType"
          label="Duration"
          value={talk.talkType}
          error={errors.talkType}
          options={TALK_TYPE_CHOICES}
          onChange={updateValue}
        />

        <Input
          type="select"
          name="audience"
          label="Intended Audience"
          value={talk.audience}
          error={errors.audience}
          options={audienceChoices.options}
          onChange={updateValue}
        />
      </Form>
    );
  }
}

export default TalkForm;
