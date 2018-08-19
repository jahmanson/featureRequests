function featureRequest(request) {
  var self = this;
  self.id = ko.observable(request.id);
  self.title = ko.observable(request.title);
  self.description = ko.observable(request.description);
  self.client = ko.observable(request.client);
  self.priority = ko.observable(request.priority);
  self.target_date = ko.observable(request.target_date);
  self.product_area = ko.observable(request.product_area);
}

function RequestsViewModel() {
  var self = this;
  self.requests = ko.observableArray([]);
  self.newTitle = ko.observable();
  self.newDescription = ko.observable();
  self.newClient = ko.observable();
  self.newPriority = ko.observable();
  self.newTargetDate = ko.observable();
  self.newProductArea = ko.observable();

  self.addRequest = function() {
    self.save();
    self.newTitle("");
    self.newDescription("");
    self.newClient("");
    self.newPriority("");
    self.newTargetDate("");
    self.newProductArea("");
  };

  self.update = function() {
    $.getJSON('/requests', function(data) {
      var featureRequests = $.map(data.db_requests, function(request) {
        return new featureRequest(request);
      })
      self.requests(featureRequests);
    })
  }

  $.getJSON('/requests', function(data) {
    var featureRequests = $.map(data.db_requests, function(request) {
      return new featureRequest(request);
    })
    self.requests(featureRequests);
  })

  self.save = function() {
    $.ajax({
      url: '/requests/new',
      contentType: 'application/json',
      type: 'POST',
      data: JSON.stringify({
        title: self.newTitle(),
        description: self.newDescription(),
        client: self.newClient(),
        priority: self.newPriority(),
        target_date: self.newTargetDate(),
        product_area: self.newProductArea()
      })
    }).done(function(data) {
      $('#featureRequestModal').modal('hide');
      self.update()
    }).fail(function() {
      $('#featureRequestModal').modal('hide');
      alert("Ajax Request Error");
    })
  };
};

ko.applyBindings(new RequestsViewModel())
