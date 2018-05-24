import React from 'react';

let inputId = 0;

const getId = () => {
  return `${inputId++}`;
};

const Option = props => <option key={props.value} value={props.value}>{props.label}</option>;

export const Select = props => {
  const { id, value, onChange, error } = props;
  const options = props.options.map(Option);
  let errorClass = '';

  if (error) {
    errorClass = 'is-danger';
  }

  return (
    <div className={`select ${errorClass} is-full-width`}>
      <select id={id} value={value} onChange={onChange}>
        {options}
      </select>
    </div>
  );
};

export const RadioButton = props => {
  const id = `${inputId++}`;
  const { name, value, label, checked, onChange, error } = props;
  let errorClass = '';

  if (error) {
    errorClass = 'is-danger';
  }

  return (
    <label className={`radio ${errorClass}`} htmlFor={id}>
      <input type="radio" id={id} name={name} value={value} checked={checked} onChange={onChange} />
      <span className="radio-text">{label}</span>
    </label>
  );
};

export const RadioGroup = props => {
  const { value, onChange, name, error } = props;
  const choices = props.choices.map(choice => {
    const checked = value === choice.value;
    return (
      <div key={choice.value}>
        <RadioButton
          {...choice}
          error={error}
          name={name}
          checked={checked}
          onChange={onChange}
        />
      </div>
    );
  });

  return <div className={`radio-group`}>{choices}</div>;
};

export const BoolInput = props => {
  const choices = [{ value: 'true', label: 'Yes' }, { value: 'false', label: 'No' }];
  return <RadioGroup {...props} choices={choices} />;
};

export const Input = props => {
  const id = getId();
  const type = props.type;
  const onChange = e => {
    let value = e.target.value;

    if (type === 'bool') {
      value = value === 'true';
    }

    props.onChange(value);
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
        value={props.value}
        onChange={onChange}
      />
    );
  } else if (type === 'bool') {
    input = <BoolInput value={props.value} error={props.error} onChange={onChange} />;
  } else if (type === 'radio-group') {
    input = (
      <RadioGroup
        value={props.value}
        error={props.error}
        choices={props.choices}
        onChange={onChange}
      />
    );
  } else if (type === 'select') {
    input = (
      <Select
        id={id}
        value={props.value}
        options={props.options}
        error={props.error}
        onChange={onChange}
      />
    );
  } else {
    input = (
      <input
        id={id}
        className={`input ${errorClass}`}
        type={props.type}
        value={props.value}
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
};

export const Form = props => {
  const { saveText = 'Save', cancelText = 'Cancel' } = props;

  return (
    <form className="form">
      {props.children}

      <div className="field is-grouped is-grouped-right">
        <div className="control">
          <button className="button is-light" type="button" onClick={props.cancel}>
            {cancelText}
          </button>
        </div>
        <div className="control">
          <button className="button is-primary" type="button" onClick={props.save}>
            {saveText}
          </button>
        </div>
      </div>
    </form>
  );
};
