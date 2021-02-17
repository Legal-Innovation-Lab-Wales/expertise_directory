import React from "react"
import {Col, Container, Form, Row} from "react-bootstrap"

export default class Filter extends React.Component {
  handleKeyUp(e) {
    const value = e.target.value.toLowerCase()
    const rows = document.querySelectorAll('#table-body tr')

    rows.forEach(row => {
      row.style.display = (row.innerText.toLowerCase().indexOf(value) > -1) ? 'table-row' : 'none'
    })
  }

  filter() {
    const filter = document.querySelector('#filter-input').value,
          department = document.querySelector('#filter-department').value

    document.querySelectorAll('#table-body tr').forEach(row => {
      row.style.display = (row.innerText.toLowerCase().indexOf(filter.toLowerCase()) > -1 &&
          (department === 'all' || row.classList.contains(department))) ? 'table-row' : 'none'
    })
  }

  render() {
    return (
      <Container>
        <Row className='filter'>
          <Col sm={8}>
            <Form>
              <Form.Group>
                <Form.Control type='text' id='filter-input' placeholder='Filter Results...' onKeyUp={this.filter.bind(this)}/>
              </Form.Group>
            </Form>
          </Col>
          <Col sm={4}>
            <Form>
              <Form.Group>
                <Form.Control as='select' id='filter-department' onChange={this.filter.bind(this)} defaultValue='all'>
                  <option value='all'>All</option>
                  { this.props.data.colleges.map(college => {
                    return [
                      <optgroup key={`${college.key}_option`} label={college.name}/>,
                      college['departments'].map(department => {
                        return <option key={`${college.key}_${department.key}_option`}
                                       value={department.key}>{department.name}</option>
                      })
                    ]
                  }) }
                </Form.Control>
              </Form.Group>
            </Form>
          </Col>
        </Row>
      </Container>
    )
  }
}