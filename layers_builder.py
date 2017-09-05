# Layer class is a map function which vinculates the *m* units from the layer (l) and link each one to the *n* units from the layer (l+1)
# the Weight matrix is composed as: rows -> units from Layer(l+1) ; columns -> units from Layer (l)
class Layer:
    
    def __init__(self, n_units_current, n_units_next=None, bias=True):
       
        self.n_units_current = n_units_current
        self.n_units_next = n_units_next
        self.bias = bias
        
        # summation vector
        self.z = self.initialize_vector(n_units_current)
                
        # activation vector
        ## just inialize the vector, afterwards process as actual activation
        self.a = self.initialize_vector(n_units_current)
        self.set_activation()        
        
        # weight matrix that connect units from current layer to next layer
        self.W = self.initialize_weights()        
        
        # delta-error vector
        self.d = self.initialize_vector(n_units_current + bias)
        
        # gradient error vector
        self.g = self.initialize_vector(n_units_current + bias)
    
    
    def initialize_weights(self):
        # case there's none next layer as the output layer, also there's no Weight matrix
        if( self.n_units_next == None):
            return np.array([])
        
        weights = np.random.randn(self.n_units_next * (self.n_units_current + self.bias))
        weights = weights.reshape(self.n_units_next, self.n_units_current + self.bias)
        return weights
        
    
    def initialize_vector(self, n_dimensions):
        return np.random.normal(size=n_dimensions)
    

    def set_activation(self):
        self.a = Utils.fun_sigmoid(self.z)
        if self.bias: self.add_activation_bias()

    
    def add_activation_bias(self):
        self.a = np.hstack((self.a, 1))

        
    def print_layer(self):
        print "W:\n %s \n" %(self.W)
        print "z: %s" %(self.z)
        print "a: %s" %(self.a)
        print "d: %s" %(self.d)
        print "g: %s" %(self.g)
        


        
# the layer output is an exception case of the Layer class   
class LayerOutput(Layer):
        def __init__(self, n_units_current):
            Layer.__init__(self, n_units_current, n_units_next=None, bias=False)




    
def net_constructer()
    if (len(layers_dim) < 2):
        sys.exit("Neural Net must have at least 2 layers")
        
    net = []
    # first stage: create input and hidden layers
    for i in np.arange(len(layers_dim) - 1, dtype=int):
        l = Layer(layers_dim[i], layers_dim[i+1])
        net.append(l)

    # second stage: create output layer
    l = LayerOutput(layers_dim[-1])
    net.append(l)
    
    return net
    