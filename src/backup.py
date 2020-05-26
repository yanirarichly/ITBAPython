union = pd.merge(self.archivo[0], self.archivo[1], on=self.column)

union = pd.concat([self.archivo[0], self.archivo[1]], axis=self.column, join='outer')

# self. archivo voy a probar de [] a {}