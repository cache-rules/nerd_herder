import React, { PureComponent } from 'react';

const Option = props => (
  <option key={props.value} value={props.value}>
    {props.label}
  </option>
);

export class Select extends PureComponent {
  render() {
    const { id, name, value, onChange, error, disabled } = this.props;
    const options = this.props.options.map(Option);
    let errorClass = '';

    if (error) {
      errorClass = 'is-danger';
    }

    return (
      <div className={`select ${errorClass} is-full-width`}>
        <select id={id} name={name} value={value} disabled={disabled} onChange={onChange}>
          {options}
        </select>
      </div>
    );}
};

export class RadioButton extends PureComponent {
  render() {
    const { id, name, value, label, checked, onChange, error, disabled } = this.props;
    let errorClass = '';

    if (error) {
      errorClass = 'is-danger';
    }

    return (
      <label className={`radio ${errorClass}`} htmlFor={id}>
        <input
          type="radio"
          id={id}
          name={name}
          value={value}
          checked={checked}
          disabled={disabled}
          onChange={onChange}
        />
        <span className="radio-text">{label}</span>
      </label>
    );
  }
};

export class RadioGroup extends PureComponent {
  render() {
    const { value, onChange, name, error, disabled } = this.props;
    const choices = this.props.choices.map((choice, idx) => {
      const checked = value === choice.value;
      const id = `${name}-idx`;
      return (
        <div key={choice.value}>
          <RadioButton
            {...choice}
            error={error}
            name={name}
            id={id}
            checked={checked}
            disabled={disabled}
            onChange={onChange}
          />
        </div>
      );
    });

    return <div className={`radio-group`}>{choices}</div>;
  }
}

export class BoolInput extends PureComponent {
  render() {
    const choices = [{ value: 'true', label: 'Yes' }, { value: 'false', label: 'No' }];
    return <RadioGroup {...this.props} choices={choices} />;
  }
}

export class Input extends PureComponent {
  render() {
    const props = this.props;
    const id = props.name;
    const type = props.type;
    const onChange = e => {
      let { name, value } = e.target;

      if (type === 'bool') {
        value = value === 'true';
      }

      props.onChange({ [name]: value });
    };
    let input = null;
    let errorClass = '';

    if (props.error) {
      errorClass = 'is-danger';
    }

    if (type === 'textarea') {
      input = (
        <textarea
          id={id}
          className={`textarea ${errorClass}`}
          name={props.name}
          value={props.value}
          disabled={props.disabled}
          onChange={onChange}
        />
      );
    } else if (type === 'bool') {
      input = (
        <BoolInput
          name={props.name}
          value={props.value}
          error={props.error}
          disabled={props.disabled}
          onChange={onChange}
        />
      );
    } else if (type === 'radio-group') {
      input = (
        <RadioGroup
          name={props.name}
          value={props.value}
          error={props.error}
          choices={props.choices}
          disabled={props.disabled}
          onChange={onChange}
        />
      );
    } else if (type === 'select') {
      input = (
        <Select
          id={id}
          name={props.name}
          value={props.value}
          options={props.options}
          error={props.error}
          disabled={props.disabled}
          onChange={onChange}
        />
      );
    } else {
      input = (
        <input
          id={id}
          className={`input ${errorClass}`}
          name={props.name}
          type={props.type}
          value={props.value}
          disabled={props.disabled}
          onChange={onChange}
        />
      );
    }

    return (
      <div className="field">
        <label htmlFor={id} className="label">
          {props.label}
        </label>

        <div className="control">{input}</div>
      </div>
    );
  }
}

export const Form = props => {
  const { saveText = 'Save', cancelText = 'Cancel', saving = false } = props;

  return (
    <form className="form">
      {props.children}

      <div className="field is-grouped is-grouped-right">
        <div className="control">
          <button
            className="button is-light"
            type="button"
            onClick={props.cancel}
            disabled={saving}
          >
            {cancelText}
          </button>
        </div>
        <div className="control">
          <button
            className="button is-primary"
            type="button"
            onClick={props.save}
            disabled={saving}
          >
            {saveText}
          </button>
        </div>
      </div>
    </form>
  );
};
