#ifndef CORRGAUSSIAN_PDF_HH
#define CORRGAUSSIAN_PDF_HH

#include "EngineCore.hh" 

class CorrGaussianPdf : public EngineCore {
public:
  CorrGaussianPdf (std::string n, Variable* _x, Variable* _y, Variable* mean1, Variable* sigma1, Variable* mean2, Variable* sigma2, Variable* correlation); 


private:

};

#endif