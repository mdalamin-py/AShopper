// Plus button click event
$(".btn-plus").click(function () {
  var id = $(this).attr("p_id").toString();
  console.log('Adding quantity for product:', id);

  $.ajax({
    type: "GET",
    url: "/pluscart",
    data: {
      product_id: id,
    },
    success: function (data) {
      // Update the DOM elements with the new data
      var quantityElement = $('#quantity'+id);

      // Check if it's an input field or text element
      if (quantityElement.is('input')) {
        quantityElement.val(data.quantity);
      } else {
        quantityElement.text(data.quantity);
      }

      $('#cart_amount'+id).text(data.item_amount);
      $('#amount').text(data.amount);
      $('#totalamount').text(data.totalamount);

      console.log('Updated quantity to:', data.quantity);
    }
  });
});


// Minus button click event
$(".btn-minus").click(function () {
  var id = $(this).attr("p_id").toString();
  console.log('Reducing quantity for product:', id);

  $.ajax({
    type: "GET",
    url: "/minuscart/",
    data: {
      product_id: id,
    },
    success: function (data) {
      // If item was removed (quantity was 1)
      if (data.removed) {
        // Fade out and remove the row
        $('#cart-item-'+id).fadeOut(300, function() {
          $(this).remove();
          // Check if cart is empty - reload to update cart count
          if (data.amount == 0) {
            window.location.href = '/cart';
          } else {
            // Reload page to update cart count in navbar
            window.location.reload();
          }
        });
      } else {
        // Update the DOM elements with the new data
        var quantityElement = $('#quantity'+id);

        // Check if it's an input field or text element
        if (quantityElement.is('input')) {
          quantityElement.val(data.quantity);
        } else {
          quantityElement.text(data.quantity);
        }

        $('#cart_amount'+id).text(data.item_amount);
      }
      $('#amount').text(data.amount);
      $('#totalamount').text(data.totalamount);

      console.log('Updated quantity to:', data.quantity);
    }
  });
});

// //Remove cart product
// $(".btn-rmv").click(function () {
//   var id = $(this).attr("p_id").toString();
//   var eml = this;
//   // console.log(id);
//   $.ajax({
//     type: "GET",
//     url: "/removecart",
//     data: {
//       product_id: id,
//     },
//     success: function (data) {
//       document.getElementById("amount").innerText = data.amount;
//       document.getElementById("totalamount").innerText = data.totalamount;
//       eml.parentNode.parentNode.parentNode.parentNode.remove();
//     },
//   });
// });

$(".btn-rmv").click(function () {
  var id = $(this).attr("p_id").toString();
  var cartRow = $('#cart-item-'+id);

  // Show confirmation
  if (!confirm('Are you sure you want to remove this item from cart?')) {
    return;
  }

  // Add fade out animation before removing
  cartRow.fadeOut(300, function() {
    // AJAX call after animation
    $.ajax({
      type: "GET",
      url: "/removecart",
      data: {
        product_id: id,
      },
      success: function (data) {
        // Remove the cart item row from DOM
        cartRow.remove();

        // Update the totals
        $('#amount').text(data.amount);
        $('#totalamount').text(data.totalamount);

        // If cart is empty, redirect to empty cart page
        // Otherwise reload to update cart count
        if (data.amount == 0) {
          window.location.href = '/cart';
        } else {
          // Reload page to update cart count in navbar
          window.location.reload();
        }
      },
      error: function() {
        // If error, show the row again
        cartRow.fadeIn(300);
        alert('Failed to remove item. Please try again.');
      }
    });
  });
});
