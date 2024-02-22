var stripe = Stripe('pk_test_51OdrStSGscJjE81TZCEgS1BpY9W15wKE8cTafnQogjLhgnEQE0UFbaCO4U987ELSd2t6ZV4wtAY2tgTBDibqmoQA00J35kFrSi');
var elements = stripe.elements();

var style = {
  base: {
    color: '#32325d',
    lineHeight: '24px',
    fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
    fontSmoothing: 'antialiased',
    fontSize: '16px',
    '::placeholder': {
      color: '#aab7c4'
    }
  },
  invalid: {
    color: '#fa755a',
    iconColor: '#fa755a'
  }
};

var card = elements.create('cardNumber', {style: style});
card.mount('#card-number');

var exp = elements.create('cardExpiry', {style: style});
exp.mount('#card-expiry');

var cvc = elements.create('cardCvc', {style: style});
cvc.mount('#card-cvc');