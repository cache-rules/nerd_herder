import React, { PureComponent } from 'react';
import { get } from "./http";

const DEFAULT_CHOICES = [{label: 'All Audiences', value: ''}];

export function withAudienceChoices(WrappedComponent) {
    class Wrapper extends PureComponent {
        constructor(props) {
            super(props);

            this.state = {
                loading: false,
                options: DEFAULT_CHOICES,
                error: null,
            }
        }

        componentDidMount() {
            this.loadChoices();
        }

        loadChoices =  async () => {
            this.setState({loading: true});
            const response = await get('/api/v1/talk-proposals/audience-choices');

            let body;

            try {
                body = await response.json();
            } catch (e) {
                console.error(e);
                this.setState({loading: false, error: 'Error loading audience choices. Try refreshing the page.'})
            }

            const options = DEFAULT_CHOICES.concat(body.map(value => ({label: value.label, value: value.id})));

            this.setState({
                options,
                loading: false,
                error: null,
            });
        };

        render() {
            return <WrappedComponent {...this.props} audienceChoices={this.state} />
        }
    }

    return Wrapper;
}
