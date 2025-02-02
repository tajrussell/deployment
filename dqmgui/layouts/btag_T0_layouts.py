def btaglayout(i, p, *rows): i["Btag/Layouts/" + p] = DQMItem(layout=rows)

btaglayout(dqmitems, "00 - Jet Properties",
 [{ 'path': "Btag/DeepFlavour_BvsAll_GLOBAL/jetMultiplicity_DeepFlavour_BvsAll_GLOBALALL",
    'description': "Jet Multiplicity ",
    'draw': { 'withref': "no" }},
  { 'path': "Btag/DeepFlavour_BvsAll_GLOBAL/jetEta_DeepFlavour_BvsAll_GLOBALALL",
    'description': "Jet Eta",
    'draw': { 'withref': "no" }},
  { 'path': "Btag/DeepCSV_BvsAll_GLOBAL/jetEta_diffEff_DeepCSV_BvsAll_GLOBALALL",
    'description': "DeepCSV Jet Eta efficiency",
    'draw': { 'withref': "no", 'ymin': '0', 'ymax': '1' }},
  { 'path': "Btag/DeepFlavour_BvsAll_GLOBAL/jetEta_diffEff_DeepFlavour_BvsAll_GLOBALALL",
    'description': "DeepFlavour Jet Eta efficiency",
    'draw': { 'withref': "no", 'ymin': '0', 'ymax': '1' }}
 ],

 [{ 'path': "Btag/DeepFlavour_BvsAll_GLOBAL/jetPt_DeepFlavour_BvsAll_GLOBALALL",
    'description': "Jet Pt ",
    'draw': { 'withref': "no" }},
  { 'path': "Btag/DeepFlavour_BvsAll_GLOBAL/jetPhi_DeepFlavour_BvsAll_GLOBALALL",
    'description': "Jet Phi",
    'draw': { 'withref': "no" }},
  { 'path': "Btag/DeepCSV_BvsAll_GLOBAL/jetPhi_diffEff_DeepCSV_BvsAll_GLOBALALL",
    'description': "DeepCSV Jet Phi efficiency",
    'draw': { 'withref': "no", 'ymin': '0', 'ymax': '1' }},
  { 'path': "Btag/DeepFlavour_BvsAll_GLOBAL/jetPhi_diffEff_DeepFlavour_BvsAll_GLOBALALL",
    'description': "DeepFlavour Jet Phi efficiency",
    'draw': { 'withref': "no", 'ymin': '0', 'ymax': '1' }}
 ],

[{ 'path': "Btag/UnifiedParticleTransformer_BvsAll_GLOBAL/jetPhi_diffEff_UnifiedParticleTransformer_BvsAll_GLOBALALL",
    'description': "UnifiedParticleTransformer Jet Phi efficiency",
    'draw': { 'withref': "no", 'ymin': '0', 'ymax': '1' }},
  { 'path': "Btag/UnifiedParticleTransformer_BvsAll_GLOBAL/jetEta_diffEff_UnifiedParticleTransformer_BvsAll_GLOBALALL",
    'description': "UnifiedParticleTransformer Jet Eta efficiency",
    'draw': { 'withref': "no", 'ymin': '0', 'ymax': '1' }},
  { 'path': "Btag/ParticleNet_BvsAll_GLOBAL/jetPhi_diffEff_ParticleNet_BvsAll_GLOBALALL",
    'description': "ParticleNet Jet Phi efficiency",
    'draw': { 'withref': "no", 'ymin': '0', 'ymax': '1' }},
  { 'path': "Btag/ParticleNet_BvsAll_GLOBAL/jetEta_diffEff_ParticleNet_BvsAll_GLOBALALL",
    'description': "ParticleNet Jet Eta efficiency",
    'draw': { 'withref': "no", 'ymin': '0', 'ymax': '1' }}
 ])


btaglayout(dqmitems, "01 - Tracks in Jet",
 [{ 'path': "Btag/IPTag_GLOBAL/selectedTrackMultVsJetPt_IPTag_GLOBALALL",
    'description': "Track Multiplicity vs Jet Pt for Selected Tracks Associated to Jets",
    'draw': { 'withref': "no", 'xmin': '25', 'drawopts': "colz" }},
  { 'path': "Btag/IPTag_GLOBAL/trackMultVsJetPt_IPTag_GLOBALALL",
    'description': "Track Multiplicity vs Jet Pt for Tracks Associated to Jets",
    'draw': { 'withref': "no", 'xmin': '25', 'drawopts': "colz" }}],

 [{ 'path': "Btag/IPTag_GLOBAL/selectedTrackQual_IPTag_GLOBALALL",
    'description': "Track Quality of Selected Tracks Associated to Jets",
    'draw': { 'withref': "no" }},
  { 'path': "Btag/IPTag_GLOBAL/trackQual_IPTag_GLOBALALL",
    'description': "Track Quality of Tracks Associated to Jets",
    'draw': { 'withref': "no" }}])


btaglayout(dqmitems, "02 - Secondary Vertex Properties",
 [{ 'path': "Btag/SV/n_sv",
    'description': "Number of secondary vertices in jet",
    'draw': { 'withref': "no" }},
  { 'path': "Btag/SV/sv_ntracks",
    'description': "Number of tracks at secondary vertex ",
   'draw': { 'withref': "no" }},
  { 'path': "Btag/SV/sv_mass",
    'description': "Mass of the secondary vertex  ",
   'draw': { 'withref': "no" }},
  { 'path': "Btag/SV/sv_pt",
    'description': "Transverse momentum of the secondary vertex",
   'draw': { 'withref': "no" }}],

 [  { 'path': "Btag/SV/sv_ptrel",
    'description': "Ratio of transverse momentum at secondary vertex over total jet transverse momentum",
   'draw': { 'withref': "no" }},
  { 'path': "Btag/SV/sv_energyratio",
    'description': "Ratio of energy at secondary vertex over total jet energy",
    'draw': { 'withref': "no" }},
  { 'path': "Btag/SV/sv_deltaR",
    'description': "Pseudoangular Distance between Jet Axis and Secondary Vertex Direction",
   'draw': { 'withref': "no" }},
  #{ 'path': "Btag/SV/sv_chi2norm",
    #'description': "Normalized Chi2 value of the secondary vertex",
   #'draw': { 'withref': "no" }},
  { 'path': "Btag/SV/sv_chi2prob",
    'description': "Chi2 probability of the secondary vertex",
   'draw': { 'withref': "no" }}])


btaglayout(dqmitems, "03 - Flight Distance Summary",
 [{ 'path': "Btag/SV/sv_dxy",
    'description': "Transverse Distance between Primary and Secondary Vertex ",
    'draw': { 'withref': "no" }},
  { 'path': "Btag/SV/sv_d3d",
    'description': "Distance between Primary and Secondary Vertex  ",
   'draw': { 'withref': "no" }}],

 [{ 'path': "Btag/SV/sv_dxysig",
    'description': "Transverse Distance Significance between Primary and Secondary vertex all jets",
    'draw': { 'withref': "no" }},
  { 'path': "Btag/SV/sv_d3dsig",
    'description': "Distance significance between primary and secondary vertex all jets ",
   'draw': { 'withref': "no" }}])

btaglayout(dqmitems, "04 - Discriminator Summary",
 [{ 'path': "Btag/JP_GLOBAL/discr_JP_GLOBALALL",
    'description': "Discriminator for JetProbability ",
    'draw': { 'withref': "no" }}
 ],

 [{ 'path': "Btag/DeepCSV_BvsAll_GLOBAL/discr_DeepCSV_BvsAll_GLOBALALL",
    'description': "Discriminator for DeepCSV BvsAll ",
    'draw': { 'withref': "no" }},
  { 'path': "Btag/DeepCSV_CvsB_GLOBAL/discr_DeepCSV_CvsB_GLOBALALL",
    'description': "Discriminator for DeepCSV CvsB ",
    'draw': { 'withref': "no" }},
  { 'path': "Btag/DeepCSV_CvsL_GLOBAL/discr_DeepCSV_CvsL_GLOBALALL",
    'description': "Discriminator for DeepCSV CvsL ",
    'draw': { 'withref': "no" }}
 ],

 [{ 'path': "Btag/DeepFlavour_BvsAll_GLOBAL/discr_DeepFlavour_BvsAll_GLOBALALL",
    'description': "Discriminator for DeepFlavour BvsAll ",
    'draw': { 'withref': "no" }},
  { 'path': "Btag/DeepFlavour_CvsB_GLOBAL/discr_DeepFlavour_CvsB_GLOBALALL",
    'description': "Discriminator for DeepFlavour CvsB ",
    'draw': { 'withref': "no" }},
  { 'path': "Btag/DeepFlavour_CvsL_GLOBAL/discr_DeepFlavour_CvsL_GLOBALALL",
    'description': "Discriminator for DeepFlavour CvsL ",
    'draw': { 'withref': "no" }}
 ]

  [{ 'path': "Btag/UnifiedParticleTransformer_BvsAll_GLOBAL/discr_UnifiedParticleTransformer_BvsAll_GLOBALALL",
    'description': "Discriminator for UnifiedParticleTransformer BvsAll ",
    'draw': { 'withref': "no" }},
  { 'path': "Btag/UnifiedParticleTransformer_BvsAll_GLOBAL/discr_UnifiedParticleTransformer_CvsB_GLOBALALL",
    'description': "Discriminator for UnifiedParticleTransformer CvsB ",
    'draw': { 'withref': "no" }},
  { 'path': "Btag/UnifiedParticleTransformer_BvsAll_GLOBAL/discr_UnifiedParticleTransformer_CvsL_GLOBALALL",
    'description': "Discriminator for UnifiedParticleTransformer CvsL ",
    'draw': { 'withref': "no" }}
 ],

  [{ 'path': "Btag/ParticleNet_BvsAll_GLOBAL/discr_ParticleNet_BvsAll_GLOBALALL",
    'description': "Discriminator for ParticleNet BvsAll ",
    'draw': { 'withref': "no" }},
  { 'path': "Btag/ParticleNet_CvsB_GLOBAL/discr_ParticleNet_CvsB_GLOBALALL",
    'description': "Discriminator for ParticleNet CvsB ",
    'draw': { 'withref': "no" }},
  { 'path': "Btag/ParticleNet_CvsL_GLOBAL/discr_ParticleNet_CvsL_GLOBALALL",
    'description': "Discriminator for ParticleNet CvsL ",
    'draw': { 'withref': "no" }}
 ])


btaglayout(dqmitems, "05 - 2D-Impact Parameter",
 [{ 'path': "Btag/IPTag_GLOBAL/ip_2D_IPTag_GLOBALALL",
    'description': "2D Impact Parameter Value",
    'draw': { 'withref': "no" }},
  { 'path': "Btag/IPTag_GLOBAL/ipe_2D_IPTag_GLOBALALL",
    'description': "2D Impact Parameter Error",
    'draw': { 'withref': "no" }},
  { 'path': "Btag/IPTag_GLOBAL/prob_2D_IPTag_GLOBALALL",
    'description': "2D Impact Parameter Probability",
    'draw': { 'withref': "no" }}],

 [{ 'path': "Btag/IPTag_GLOBAL/tkNHits_2D_IPTag_GLOBALALL",
    'description': "# of Hits in Tracks used in 2D Impact Parameter",
    'draw': { 'withref': "no" }},
  { 'path': "Btag/IPTag_GLOBAL/tkNChiSqr_2D_IPTag_GLOBALALL",
    'description': "Chi2Sq of Tracks used in 2D Impact Parameter",
    'draw': { 'withref': "no" }},
  { 'path': "Btag/IPTag_GLOBAL/decLen_2D_IPTag_GLOBALALL",
    'description': "2D Decay Length",
    'draw': { 'withref': "no" }},
  { 'path': "Btag/IPTag_GLOBAL/jetDist_2D_IPTag_GLOBALALL",
    'description': "2D Jet Distance",
    'draw': { 'withref': "no" }}])


btaglayout(dqmitems, "06 - 3D-Impact Parameter",
 [{ 'path': "Btag/IPTag_GLOBAL/ip_3D_IPTag_GLOBALALL",
    'description': "3D Impact Parameter Value",
    'draw': { 'withref': "no" }},
  { 'path': "Btag/IPTag_GLOBAL/ipe_3D_IPTag_GLOBALALL",
    'description': "3D Impact Parameter Error",
    'draw': { 'withref': "no" }},
  { 'path': "Btag/IPTag_GLOBAL/prob_3D_IPTag_GLOBALALL",
    'description': "3D Impact Parameter Probability",
    'draw': { 'withref': "no" }},
  { 'path': "Btag/IPTag_GLOBAL/ips_3D_IPTag_GLOBALALL",
    'description': "3D Impact Parameter Significance",
    'draw': { 'withref': "no" }},
  { 'path': "Btag/IPTag_GLOBAL/ips1_3D_IPTag_GLOBALALL",
    'description': "3D Impact Parameter Significance 1-Track",
    'draw': { 'withref': "no" }}],

 [{ 'path': "Btag/IPTag_GLOBAL/tkPt_3D_IPTag_GLOBALALL",
    'description': "Pt 3D of Tracks used in 3D Impact Parameter",
    'draw': { 'withref': "no" }},
  { 'path': "Btag/IPTag_GLOBAL/tkNChiSqr_3D_IPTag_GLOBALALL",
    'description': "Chi2Sq of Tracks used in 3D Impact Parameter",
    'draw': { 'withref': "no" }},
  { 'path': "Btag/IPTag_GLOBAL/tkNHits_3D_IPTag_GLOBALALL",
    'description': "# of Hits in Tracks used in 3D Impact Parameter",
    'draw': { 'withref': "no" }},
  { 'path': "Btag/IPTag_GLOBAL/decLen_3D_IPTag_GLOBALALL",
    'description': "3D Decay Length",
    'draw': { 'withref': "no" }},
  { 'path': "Btag/IPTag_GLOBAL/jetDist_3D_IPTag_GLOBALALL",
    'description': "3D Jet Distance",
    'draw': { 'withref': "no" }}])


btaglayout(dqmitems, "07 - ROC Curves",
 [{ 'path': "Btag/DeepCSV_BvsAll_GLOBAL/FlavEffVsBEff_DUSG_discr_DeepCSV_BvsAll_GLOBAL",
    'overlays': ["Btag/DeepCSV_BvsAll_GLOBAL/FlavEffVsBEff_C_discr_DeepCSV_BvsAll_GLOBAL"],
    'description': "DeepCSV ROC Curve BvsAll",
    'draw': {'withref': "no", 'xmin': '0.1', 'xmax': '1', 'xtype': 'log', 'ytype': 'log'}},
  { 'path': "Btag/DeepCSV_CvsB_GLOBAL/FlavEffVsCEff_DUSG_discr_DeepCSV_CvsB_GLOBAL",
    'overlays': ["Btag/DeepCSV_CvsB_GLOBAL/FlavEffVsCEff_B_discr_DeepCSV_CvsB_GLOBAL"],
    'description': "DeepCSV ROC Curve CvsB",
    'draw': {'withref': "no", 'xmin': '0.1', 'xmax': '1', 'xtype': 'log', 'ytype': 'log'}},
  { 'path': "Btag/DeepCSV_CvsL_GLOBAL/FlavEffVsCEff_DUSG_discr_DeepCSV_CvsL_GLOBAL",
    'overlays': ["Btag/DeepCSV_CvsL_GLOBAL/FlavEffVsCEff_B_discr_DeepCSV_CvsL_GLOBAL"],
    'description': "DeepCSV ROC Curve CvsL",
    'draw': {'withref': "no", 'xmin': '0.1', 'xmax': '1', 'xtype': 'log', 'ytype': 'log'}},
 ],

 [{ 'path': "Btag/DeepFlavour_BvsAll_GLOBAL/FlavEffVsBEff_DUSG_discr_DeepFlavour_BvsAll_GLOBAL",
    'overlays': ["Btag/DeepFlavour_BvsAll_GLOBAL/FlavEffVsBEff_C_discr_DeepFlavour_BvsAll_GLOBAL"],
    'description': "DeepFlavour ROC Curve BvsAll",
    'draw': {'withref': "no", 'xmin': '0.1', 'xmax': '1', 'xtype': 'log', 'ytype': 'log'}},
  { 'path': "Btag/DeepFlavour_CvsB_GLOBAL/FlavEffVsCEff_DUSG_discr_DeepFlavour_CvsB_GLOBAL",
    'overlays': ["Btag/DeepFlavour_CvsB_GLOBAL/FlavEffVsCEff_B_discr_DeepFlavour_CvsB_GLOBAL"],
    'description': "DeepFlavour ROC Curve CvsB",
    'draw': {'withref': "no", 'xmin': '0.1', 'xmax': '1', 'xtype': 'log', 'ytype': 'log'}},
  { 'path': "Btag/DeepFlavour_CvsL_GLOBAL/FlavEffVsCEff_DUSG_discr_DeepFlavour_CvsL_GLOBAL",
    'overlays': ["Btag/DeepFlavour_CvsL_GLOBAL/FlavEffVsCEff_B_discr_DeepFlavour_CvsL_GLOBAL"],
    'description': "DeepFlavour ROC Curve CvsL",
    'draw': {'withref': "no", 'xmin': '0.1', 'xmax': '1', 'xtype': 'log', 'ytype': 'log'}},
 ],

 [{ 'path': "Btag/UnifiedParticleTransformer_BvsAll_GLOBAL/FlavEffVsBEff_DUSG_discr_UnifiedParticleTransformer_BvsAll_GLOBAL",
    'overlays': ["Btag/UnifiedParticleTransformer_BvsAll_GLOBAL/FlavEffVsBEff_C_discr_UnifiedParticleTransformer_BvsAll_GLOBAL"],
    'description': "UnifiedParticleTransformer ROC Curve BvsAll",
    'draw': {'withref': "no", 'xmin': '0.1', 'xmax': '1', 'xtype': 'log', 'ytype': 'log'}},
  { 'path': "Btag/UnifiedParticleTransformer_CvsB_GLOBAL/FlavEffVsCEff_DUSG_discr_UnifiedParticleTransformer_CvsB_GLOBAL",
    'overlays': ["Btag/UnifiedParticleTransformer_CvsB_GLOBAL/FlavEffVsCEff_B_discr_UnifiedParticleTransformer_CvsB_GLOBAL"],
    'description': "UnifiedParticleTransformer ROC Curve CvsB",
    'draw': {'withref': "no", 'xmin': '0.1', 'xmax': '1', 'xtype': 'log', 'ytype': 'log'}},
  { 'path': "Btag/UnifiedParticleTransformer_CvsL_GLOBAL/FlavEffVsCEff_DUSG_discr_UnifiedParticleTransformer_CvsL_GLOBAL",
    'overlays': ["Btag/UnifiedParticleTransformer_CvsL_GLOBAL/FlavEffVsCEff_B_discr_UnifiedParticleTransformer_CvsL_GLOBAL"],
    'description': "UnifiedParticleTransformer ROC Curve CvsL",
    'draw': {'withref': "no", 'xmin': '0.1', 'xmax': '1', 'xtype': 'log', 'ytype': 'log'}},
 ],

 [{ 'path': "Btag/ParticleNet_BvsAll_GLOBAL/FlavEffVsBEff_DUSG_discr_ParticleNet_BvsAll_GLOBAL",
    'overlays': ["Btag/ParticleNet_BvsAll_GLOBAL/FlavEffVsBEff_C_discr_ParticleNet_BvsAll_GLOBAL"],
    'description': "ParticleNet ROC Curve BvsAll",
    'draw': {'withref': "no", 'xmin': '0.1', 'xmax': '1', 'xtype': 'log', 'ytype': 'log'}},
  { 'path': "Btag/ParticleNet_CvsB_GLOBAL/FlavEffVsCEff_DUSG_discr_ParticleNet_CvsB_GLOBAL",
    'overlays': ["Btag/ParticleNet_CvsB_GLOBAL/FlavEffVsCEff_B_discr_ParticleNet_CvsB_GLOBAL"],
    'description': "ParticleNet ROC Curve CvsB",
    'draw': {'withref': "no", 'xmin': '0.1', 'xmax': '1', 'xtype': 'log', 'ytype': 'log'}},
  { 'path': "Btag/ParticleNet_CvsL_GLOBAL/FlavEffVsCEff_DUSG_discr_DeepFlavour_CvsL_GLOBAL",
    'overlays': ["Btag/ParticleNet_CvsL_GLOBAL/FlavEffVsCEff_B_discr_ParticleNet_CvsL_GLOBAL"],
    'description': "ParticleNet ROC Curve CvsL",
    'draw': {'withref': "no", 'xmin': '0.1', 'xmax': '1', 'xtype': 'log', 'ytype': 'log'}},
 ])
