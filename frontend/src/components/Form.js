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
  onChange = (e) => {
    const { type, onChange } = this.props;
    const name = e.target.name;
    let value = e.target.value;

      if (type === 'bool') {
        value = value === 'true';
      }

      onChange({ [name]: value });
  };

  render() {
    const { type, name, label, value, error, disabled, choices, options, required } = this.props;
    let input = null;
    let errorClass = '';

    if (error) {
      errorClass = 'is-danger';
    }

    if (type === 'textarea') {
      input = (
        <textarea
          id={name}
          className={`textarea ${errorClass}`}
          name={name}
          value={value}
          disabled={disabled}
          onChange={this.onChange}
        />
      );
    } else if (type === 'bool') {
      input = (
        <BoolInput
          name={name}
          value={value}
          error={error}
          disabled={disabled}
          onChange={this.onChange}
        />
      );
    } else if (type === 'radio-group') {
      input = (
        <RadioGroup
          name={name}
          value={value}
          error={error}
          choices={choices}
          disabled={disabled}
          onChange={this.onChange}
        />
      );
    } else if (type === 'select') {
      input = (
        <Select
          id={name}
          name={name}
          value={value}
          options={options}
          error={error}
          disabled={disabled}
          onChange={this.onChange}
        />
      );
    } else {
      input = (
        <input
          id={name}
          className={`input ${errorClass}`}
          name={name}
          type={type}
          value={value}
          disabled={disabled}
          onChange={this.onChange}
        />
      );
    }

    return (
      <div className="field">
        <label htmlFor={name} className="label">
          {label}{required ? '*' : ''}
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
