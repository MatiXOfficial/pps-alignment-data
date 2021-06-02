/****************************************************************************
* Author: 
*  Mateusz Kocot (mateuszkocot99@gmail.com)
*  
* Description: 
*  A simple module to convert old distributions.root files (before 2018) with histograms 
*  needed for the harvester, to the new standard.
****************************************************************************/

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

#include "TFile.h"
#include "TKey.h"
#include "TH1D.h"
#include "TProfile.h"

#include <memory>

class PPSLegacyDistributionsConverter : public edm::one::EDAnalyzer<> {
public:
  explicit PPSLegacyDistributionsConverter(const edm::ParameterSet &); 
  static void fillDescriptions(edm::ConfigurationDescriptions &descriptions);

private:
  void analyze(const edm::Event &, const edm::EventSetup &) override;

  static void copyRecursively(TDirectory *oldDir, TDirectory *newDir);

  std::string filePath;
};


PPSLegacyDistributionsConverter::PPSLegacyDistributionsConverter(const edm::ParameterSet &iConfig)
    : filePath(iConfig.getParameter<std::string>("file_path")) {}


void PPSLegacyDistributionsConverter::fillDescriptions(edm::ConfigurationDescriptions &descriptions) {
  edm::ParameterSetDescription desc;
  desc.add<std::string>("file_path", "distributions.root");
  descriptions.addWithDefaultLabel(desc);
}


void PPSLegacyDistributionsConverter::analyze(const edm::Event &iEvent, const edm::EventSetup &iSetup) {
  TFile *oldFile = TFile::Open(filePath.c_str());
  TFile *newFile = new TFile("new_distributions.root", "recreate");

  for (std::string sectorName : {"sector 45", "sector 56"}) {
    TDirectory *oldSectorDir = (TDirectory *)oldFile->Get(sectorName.c_str());
    TDirectory *newSectorDir = newFile->mkdir(sectorName.c_str());

    // near_far folder
    TDirectory *oldNearFarDir = (TDirectory *)oldSectorDir->Get("near_far");
    TDirectory *newNearFarDir = newSectorDir->mkdir("near_far");
    gDirectory = newNearFarDir;

    // profile plots
    for (std::string profileName : {"p_x_diffFN_vs_x_N", "p_y_diffFN_vs_y_N", "p_y_diffFN_vs_y_F"}) {
      TProfile *profile = (TProfile *)oldNearFarDir->Get(profileName.c_str());
      profile->Write(profileName.c_str());
    }

    // slice plots
    for (std::string RPLabel : {"N", "F"}) {
      TDirectory *oldSlicesDir = 
          (TDirectory *)oldNearFarDir->Get(("p_y_diffFN_vs_y_" + RPLabel + ", x slices").c_str());
      TDirectory *newSlicesDir = newNearFarDir->mkdir(("x slices, " + RPLabel).c_str());

      TIter next(oldSlicesDir->GetListOfKeys());
      TObject *o;
      while ((o = next())) {
        TKey *k = (TKey *)o;

        std::string name = k->GetName();
        gDirectory = newSlicesDir->mkdir(name.c_str());

        // p_y_diffFN_vs_y
        TProfile *p_y_diffFN_vs_y = (TProfile *)k->ReadObj();
        p_y_diffFN_vs_y->Write("p_y_diffFN_vs_y");

        // h_y
        TH1D *h_y = p_y_diffFN_vs_y->ProjectionX("h_y", "B");
        h_y->Write("h_y");
      }
    }

    // the rest of the folders
    for (std::string folderName : {"before selection", "cuts", "after selection", "profiles"}) {
      copyRecursively((TDirectory *)oldSectorDir->Get(folderName.c_str()), newSectorDir->mkdir(folderName.c_str()));
    }
  }
}

void PPSLegacyDistributionsConverter::copyRecursively(TDirectory *oldDir, TDirectory *newDir) {
  gDirectory = newDir;

  TIter next = (oldDir->GetListOfKeys());
  TObject *o;

  // browse oldDir
  while ((o = next())) {
    TKey *k = (TKey *)o;
    if (o->IsFolder()) {   // if directory, go deeper
      copyRecursively((TDirectory *)k->ReadObj(), newDir->mkdir(k->GetName()));
    } else {               // if a file, copy
      k->ReadObj()->Write(k->GetName());
    }
  }

  gDirectory = newDir->GetMotherDir();  // go back to the mother directory
}


DEFINE_FWK_MODULE(PPSLegacyDistributionsConverter);
