client.test('Request executed successfully', function () {
  const validateExpression = !!response.status.toString().match(/20\d/)
  client.assert(validateExpression, 'Response status is not 2xx')
})
