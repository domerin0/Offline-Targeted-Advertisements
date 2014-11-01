class Fisherfaces(Model):

    def __init__(self, X=None, y=None, num_components=None, k=1):
        Model.__init__(self, name="Fisherfaces")
        self.k = k
        self.num_components = num_components
        try:
            self.compute(X,y)
        except:
            pass


    def compute(self, X, y):
        """ Compute the Fisherfaces as described in [BHK1997]: Wpcafld = Wpca * Wfld.

        Args:
            X [dim x num_data] input data
            y [1 x num_data] classes
        """
        n = len(y)
        c = len(np.unique(y))
        pca = PCA(X, n-c)
        lda = LDA(pca.project(X), y, self.num_components)
        self._eigenvectors = pca.W*lda.W
        self.num_components = lda.num_components
        self.P = self.project(X)
        self.y = y

    def predict(self, X):
        Q = self.project(X)
        return NearestNeighbor.predict(self.P, Q, self.y, k=self.k)

    def project(self, X):
        return np.dot(self._eigenvectors.T, X)

    def reconstruct(self, X):
        return np.dot(self._eigenvectors, X)
