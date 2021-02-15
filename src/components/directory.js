import React from 'react'
import {Col, Container, Row} from 'react-bootstrap'
import './directory.css'

function DirectoryRow(props) {
  return (
    <tr>
      <td nowrap='true' className='staff-name'>
        <a href={props.staff_member.url} target='_blank'>{props.staff_member.name}</a></td>
      <td>{props.staff_member.expertise}</td>
    </tr>
  )
}

export default class Directory extends React.Component {
  constructor(props) {
    super(props)

    this.state = {
      last_update: '',
      law: []
    }
  }

  handleKeyUp(e) {
    const value = e.target.value.toLowerCase();
    const rows = document.querySelectorAll('#table-body tr');

    rows.forEach(row => {
      row.style.display = (row.innerText.toLowerCase().indexOf(value) > -1) ? 'table-row' : 'none'
    });
  }

  componentDidMount() {
    fetch('/expertise.json')
        .then(response => response.json())
        .then(data => {
          this.setState({...this.state, ...data})
        })
        .catch(err => console.error(err))
  }

  render() {
    return (
        <Container>
          <Row>
            <Col xs={12}>
              <h1 className='title text-center'><strong>Directory of Expertise</strong></h1>
              <h5 className='text-center'>This is a quick proof of concept that automatically collates the Areas of
                Expertise from staff's profile pages on the main University website.</h5>
              <div className='mx-auto filter-div'>
                <input id='filter-input' type='text' className='form-control' placeholder='Filter Results...'
                       onKeyUp={(e) => {this.handleKeyUp(e)}}/>
              </div>
              <div>Last Updated at: {this.state.last_update}</div>
              <table id='table' className='expertise-table table'>
                <thead>
                <tr>
                  <th scope='col'>Name</th>
                  <th scope='col'>Expertise</th>
                </tr>
                </thead>
                <tbody id='table-body'>
                  { this.state.law.map(staff_member => <DirectoryRow key={staff_member.name} staff_member={staff_member}/>) }
                </tbody>
              </table>
            </Col>
          </Row>
        </Container>
    )
  }
}