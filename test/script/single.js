client.test('Request executed successfully', function () {
    const validateExpression = !!response.status.toString().match(/20\d/)
    client.assert(validateExpression, 'Response status is not 2xx')
})
client.test("Response should be a JSON object", function () {
    client.assert(response.body !== null, "Response body is null");
    client.assert(typeof response.body === "object", "Response is not a JSON object");
});
