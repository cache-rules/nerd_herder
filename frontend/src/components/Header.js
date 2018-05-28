import React, { PureComponent } from 'react';
import { Link } from 'react-router-dom';
import './Header.css';

class Header extends PureComponent {
  render() {
    const { pathname } = this.props.location;
    let navClass = 'nav--fixed';

    if (pathname === '/') {
      navClass = 'nav--transparent';
    }

    return (
      <nav className={`${navClass} navbar is-fixed-top`}>
        <div className="container">
          <div className="navbar-brand">
            <div className="navbar-item">
              <Link className="nav-link" to="/">
                <div className="nav-icon">
                  <i className="fab fa-python fa-3x" />
                </div>

                <div className="nav-title">
                  <h3 className="is-size-4 has-text-weight-bold">PuPPy</h3>
                  <p className="is-size-7 is-uppercase">Puget Sound Programming Python</p>
                </div>
              </Link>
            </div>
          </div>
        </div>
      </nav>
    );
  }
}

export default Header;
