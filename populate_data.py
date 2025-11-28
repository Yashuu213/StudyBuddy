import json

def create_full_data():
    data = {
        "classes": [
            {
                "id": "11",
                "name": "Class 11",
                "subjects": [
                    {
                        "id": "physics",
                        "name": "Physics",
                        "chapters": [
                            {"id": "ch1", "name": "Units and Measurements", "topics": [{"id": "t1", "name": "International System of Units"}, {"id": "t2", "name": "Measurement of Length, Mass, Time"}, {"id": "t3", "name": "Accuracy and Precision"}, {"id": "t4", "name": "Dimensional Analysis"}]},
                            {"id": "ch2", "name": "Motion in a Straight Line", "topics": [{"id": "t1", "name": "Position, Path Length, Displacement"}, {"id": "t2", "name": "Average Velocity and Speed"}, {"id": "t3", "name": "Instantaneous Velocity and Speed"}, {"id": "t4", "name": "Acceleration"}, {"id": "t5", "name": "Kinematic Equations"}]},
                            {"id": "ch3", "name": "Motion in a Plane", "topics": [{"id": "t1", "name": "Scalars and Vectors"}, {"id": "t2", "name": "Multiplication of Vectors"}, {"id": "t3", "name": "Projectile Motion"}, {"id": "t4", "name": "Uniform Circular Motion"}]},
                            {"id": "ch4", "name": "Laws of Motion", "topics": [{"id": "t1", "name": "Newton's First Law"}, {"id": "t2", "name": "Newton's Second Law"}, {"id": "t3", "name": "Newton's Third Law"}, {"id": "t4", "name": "Conservation of Momentum"}, {"id": "t5", "name": "Friction"}]},
                            {"id": "ch5", "name": "Work, Energy and Power", "topics": [{"id": "t1", "name": "Work-Energy Theorem"}, {"id": "t2", "name": "Kinetic Energy"}, {"id": "t3", "name": "Potential Energy"}, {"id": "t4", "name": "Conservation of Mechanical Energy"}, {"id": "t5", "name": "Collisions"}]},
                            {"id": "ch6", "name": "System of Particles and Rotational Motion", "topics": [{"id": "t1", "name": "Centre of Mass"}, {"id": "t2", "name": "Torque and Angular Momentum"}, {"id": "t3", "name": "Moment of Inertia"}, {"id": "t4", "name": "Rolling Motion"}]},
                            {"id": "ch7", "name": "Gravitation", "topics": [{"id": "t1", "name": "Kepler's Laws"}, {"id": "t2", "name": "Universal Law of Gravitation"}, {"id": "t3", "name": "Gravitational Potential Energy"}, {"id": "t4", "name": "Escape Speed"}, {"id": "t5", "name": "Earth Satellites"}]},
                            {"id": "ch8", "name": "Mechanical Properties of Solids", "topics": [{"id": "t1", "name": "Stress and Strain"}, {"id": "t2", "name": "Hooke's Law"}, {"id": "t3", "name": "Young's Modulus"}]},
                            {"id": "ch9", "name": "Mechanical Properties of Fluids", "topics": [{"id": "t1", "name": "Pascal's Law"}, {"id": "t2", "name": "Bernoulli's Principle"}, {"id": "t3", "name": "Viscosity"}, {"id": "t4", "name": "Surface Tension"}]},
                            {"id": "ch10", "name": "Thermal Properties of Matter", "topics": [{"id": "t1", "name": "Thermal Expansion"}, {"id": "t2", "name": "Specific Heat Capacity"}, {"id": "t3", "name": "Calorimetry"}, {"id": "t4", "name": "Heat Transfer"}]},
                            {"id": "ch11", "name": "Thermodynamics", "topics": [{"id": "t1", "name": "Zeroth Law"}, {"id": "t2", "name": "First Law of Thermodynamics"}, {"id": "t3", "name": "Second Law of Thermodynamics"}, {"id": "t4", "name": "Carnot Engine"}]},
                            {"id": "ch12", "name": "Kinetic Theory", "topics": [{"id": "t1", "name": "Molecular Nature of Matter"}, {"id": "t2", "name": "Law of Equipartition of Energy"}, {"id": "t3", "name": "Specific Heat Capacity"}]},
                            {"id": "ch13", "name": "Oscillations", "topics": [{"id": "t1", "name": "Simple Harmonic Motion"}, {"id": "t2", "name": "Energy in SHM"}, {"id": "t3", "name": "Simple Pendulum"}]},
                            {"id": "ch14", "name": "Waves", "topics": [{"id": "t1", "name": "Transverse and Longitudinal Waves"}, {"id": "t2", "name": "Speed of Wave"}, {"id": "t3", "name": "Superposition Principle"}, {"id": "t4", "name": "Beats"}, {"id": "t5", "name": "Doppler Effect"}]}
                        ]
                    },
                    {
                        "id": "chemistry",
                        "name": "Chemistry",
                        "chapters": [
                            {"id": "ch1", "name": "Some Basic Concepts of Chemistry", "topics": [{"id": "t1", "name": "Mole Concept"}, {"id": "t2", "name": "Stoichiometry"}]},
                            {"id": "ch2", "name": "Structure of Atom", "topics": [{"id": "t1", "name": "Bohr's Model"}, {"id": "t2", "name": "Quantum Mechanical Model"}]},
                            {"id": "ch3", "name": "Classification of Elements", "topics": [{"id": "t1", "name": "Periodic Trends"}]},
                            {"id": "ch4", "name": "Chemical Bonding", "topics": [{"id": "t1", "name": "VSEPR Theory"}, {"id": "t2", "name": "Hybridisation"}, {"id": "t3", "name": "MOT"}]},
                            {"id": "ch5", "name": "Thermodynamics", "topics": [{"id": "t1", "name": "Enthalpy"}, {"id": "t2", "name": "Entropy"}, {"id": "t3", "name": "Gibbs Energy"}]},
                            {"id": "ch6", "name": "Equilibrium", "topics": [{"id": "t1", "name": "Le Chatelier's Principle"}, {"id": "t2", "name": "pH Concept"}]},
                            {"id": "ch7", "name": "Redox Reactions", "topics": [{"id": "t1", "name": "Oxidation Number"}, {"id": "t2", "name": "Balancing Redox Reactions"}]},
                            {"id": "ch8", "name": "Organic Chemistry: Basic Principles", "topics": [{"id": "t1", "name": "IUPAC Nomenclature"}, {"id": "t2", "name": "Isomerism"}, {"id": "t3", "name": "Reaction Mechanisms"}]},
                            {"id": "ch9", "name": "Hydrocarbons", "topics": [{"id": "t1", "name": "Alkanes"}, {"id": "t2", "name": "Alkenes"}, {"id": "t3", "name": "Alkynes"}, {"id": "t4", "name": "Aromatic Hydrocarbons"}]}
                        ]
                    },
                    {
                        "id": "maths",
                        "name": "Mathematics",
                        "chapters": [
                            {"id": "ch1", "name": "Sets", "topics": [{"id": "t1", "name": "Types of Sets"}, {"id": "t2", "name": "Venn Diagrams"}]},
                            {"id": "ch2", "name": "Relations and Functions", "topics": [{"id": "t1", "name": "Domain and Range"}, {"id": "t2", "name": "Types of Functions"}]},
                            {"id": "ch3", "name": "Trigonometric Functions", "topics": [{"id": "t1", "name": "Trigonometric Identities"}, {"id": "t2", "name": "Trigonometric Equations"}]},
                            {"id": "ch4", "name": "Complex Numbers", "topics": [{"id": "t1", "name": "Algebra of Complex Numbers"}, {"id": "t2", "name": "Argand Plane"}]},
                            {"id": "ch5", "name": "Linear Inequalities", "topics": [{"id": "t1", "name": "Graphical Solution"}]},
                            {"id": "ch6", "name": "Permutations and Combinations", "topics": [{"id": "t1", "name": "Fundamental Principle of Counting"}, {"id": "t2", "name": "nPr and nCr"}]},
                            {"id": "ch7", "name": "Binomial Theorem", "topics": [{"id": "t1", "name": "General Term"}]},
                            {"id": "ch8", "name": "Sequence and Series", "topics": [{"id": "t1", "name": "AP and GP"}]},
                            {"id": "ch9", "name": "Straight Lines", "topics": [{"id": "t1", "name": "Slope of a Line"}, {"id": "t2", "name": "Forms of Line Equation"}]},
                            {"id": "ch10", "name": "Conic Sections", "topics": [{"id": "t1", "name": "Circle"}, {"id": "t2", "name": "Parabola"}, {"id": "t3", "name": "Ellipse"}, {"id": "t4", "name": "Hyperbola"}]},
                            {"id": "ch11", "name": "Introduction to 3D Geometry", "topics": [{"id": "t1", "name": "Distance Formula"}, {"id": "t2", "name": "Section Formula"}]},
                            {"id": "ch12", "name": "Limits and Derivatives", "topics": [{"id": "t1", "name": "Limits"}, {"id": "t2", "name": "Derivatives"}]},
                            {"id": "ch13", "name": "Statistics", "topics": [{"id": "t1", "name": "Mean Deviation"}, {"id": "t2", "name": "Variance and Standard Deviation"}]},
                            {"id": "ch14", "name": "Probability", "topics": [{"id": "t1", "name": "Events"}, {"id": "t2", "name": "Axiomatic Approach"}]}
                        ]
                    }
                ]
            },
            {
                "id": "12",
                "name": "Class 12",
                "subjects": [
                    {
                        "id": "physics",
                        "name": "Physics",
                        "chapters": [
                            {"id": "ch1", "name": "Electric Charges and Fields", "topics": [{"id": "t1", "name": "Coulomb's Law"}, {"id": "t2", "name": "Electric Field"}, {"id": "t3", "name": "Electric Flux"}, {"id": "t4", "name": "Gauss's Law"}]},
                            {"id": "ch2", "name": "Electrostatic Potential and Capacitance", "topics": [{"id": "t1", "name": "Potential due to Point Charge"}, {"id": "t2", "name": "Equipotential Surfaces"}, {"id": "t3", "name": "Capacitors"}, {"id": "t4", "name": "Energy Stored in Capacitor"}]},
                            {"id": "ch3", "name": "Current Electricity", "topics": [{"id": "t1", "name": "Ohm's Law"}, {"id": "t2", "name": "Drift Velocity"}, {"id": "t3", "name": "Kirchhoff's Rules"}, {"id": "t4", "name": "Wheatstone Bridge"}, {"id": "t5", "name": "Potentiometer"}]},
                            {"id": "ch4", "name": "Moving Charges and Magnetism", "topics": [{"id": "t1", "name": "Biot-Savart Law"}, {"id": "t2", "name": "Ampere's Circuital Law"}, {"id": "t3", "name": "Force on a Moving Charge"}, {"id": "t4", "name": "Cyclotron"}]},
                            {"id": "ch5", "name": "Magnetism and Matter", "topics": [{"id": "t1", "name": "Bar Magnet"}, {"id": "t2", "name": "Earth's Magnetism"}, {"id": "t3", "name": "Magnetic Properties of Materials"}]},
                            {"id": "ch6", "name": "Electromagnetic Induction", "topics": [{"id": "t1", "name": "Faraday's Law"}, {"id": "t2", "name": "Lenz's Law"}, {"id": "t3", "name": "Eddy Currents"}, {"id": "t4", "name": "Self and Mutual Induction"}]},
                            {"id": "ch7", "name": "Alternating Current", "topics": [{"id": "t1", "name": "AC Voltage applied to Resistor/Inductor/Capacitor"}, {"id": "t2", "name": "LCR Circuit"}, {"id": "t3", "name": "Resonance"}, {"id": "t4", "name": "Transformers"}]},
                            {"id": "ch8", "name": "Electromagnetic Waves", "topics": [{"id": "t1", "name": "Displacement Current"}, {"id": "t2", "name": "EM Spectrum"}]},
                            {"id": "ch9", "name": "Ray Optics and Optical Instruments", "topics": [{"id": "t1", "name": "Reflection"}, {"id": "t2", "name": "Refraction"}, {"id": "t3", "name": "Total Internal Reflection"}, {"id": "t4", "name": "Lenses"}, {"id": "t5", "name": "Prism"}, {"id": "t6", "name": "Microscope and Telescope"}]},
                            {"id": "ch10", "name": "Wave Optics", "topics": [{"id": "t1", "name": "Huygens Principle"}, {"id": "t2", "name": "Interference (Young's Experiment)"}, {"id": "t3", "name": "Diffraction"}, {"id": "t4", "name": "Polarisation"}]},
                            {"id": "ch11", "name": "Dual Nature of Radiation and Matter", "topics": [{"id": "t1", "name": "Photoelectric Effect"}, {"id": "t2", "name": "Einstein's Photoelectric Equation"}, {"id": "t3", "name": "de Broglie Hypothesis"}]},
                            {"id": "ch12", "name": "Atoms", "topics": [{"id": "t1", "name": "Alpha-particle Scattering"}, {"id": "t2", "name": "Bohr Model"}, {"id": "t3", "name": "Hydrogen Spectrum"}]},
                            {"id": "ch13", "name": "Nuclei", "topics": [{"id": "t1", "name": "Mass-Energy Relation"}, {"id": "t2", "name": "Radioactivity"}, {"id": "t3", "name": "Nuclear Fission and Fusion"}]},
                            {"id": "ch14", "name": "Semiconductor Electronics", "topics": [{"id": "t1", "name": "Intrinsic and Extrinsic Semiconductors"}, {"id": "t2", "name": "PN Junction Diode"}, {"id": "t3", "name": "Rectifiers"}, {"id": "t4", "name": "Logic Gates"}]}
                        ]
                    },
                    {
                        "id": "chemistry",
                        "name": "Chemistry",
                        "chapters": [
                            {"id": "ch1", "name": "Solutions", "topics": [{"id": "t1", "name": "Types of Solutions"}, {"id": "t2", "name": "Raoult's Law"}, {"id": "t3", "name": "Colligative Properties"}]},
                            {"id": "ch2", "name": "Electrochemistry", "topics": [{"id": "t1", "name": "Nernst Equation"}, {"id": "t2", "name": "Conductance"}, {"id": "t3", "name": "Batteries and Fuel Cells"}]},
                            {"id": "ch3", "name": "Chemical Kinetics", "topics": [{"id": "t1", "name": "Rate of Reaction"}, {"id": "t2", "name": "Order and Molecularity"}, {"id": "t3", "name": "Arrhenius Equation"}]},
                            {"id": "ch4", "name": "d and f Block Elements", "topics": [{"id": "t1", "name": "General Properties"}, {"id": "t2", "name": "Lanthanoids and Actinoids"}]},
                            {"id": "ch5", "name": "Coordination Compounds", "topics": [{"id": "t1", "name": "Werner's Theory"}, {"id": "t2", "name": "Nomenclature"}, {"id": "t3", "name": "Isomerism"}, {"id": "t4", "name": "CFT"}]},
                            {"id": "ch6", "name": "Haloalkanes and Haloarenes", "topics": [{"id": "t1", "name": "Nomenclature"}, {"id": "t2", "name": "SN1 and SN2 Mechanisms"}]},
                            {"id": "ch7", "name": "Alcohols, Phenols and Ethers", "topics": [{"id": "t1", "name": "Preparation and Properties"}, {"id": "t2", "name": "Dehydration of Alcohols"}]},
                            {"id": "ch8", "name": "Aldehydes, Ketones and Carboxylic Acids", "topics": [{"id": "t1", "name": "Nucleophilic Addition"}, {"id": "t2", "name": "Aldol Condensation"}, {"id": "t3", "name": "Cannizzaro Reaction"}]},
                            {"id": "ch9", "name": "Amines", "topics": [{"id": "t1", "name": "Basicity of Amines"}, {"id": "t2", "name": "Diazonium Salts"}]},
                            {"id": "ch10", "name": "Biomolecules", "topics": [{"id": "t1", "name": "Carbohydrates"}, {"id": "t2", "name": "Proteins"}, {"id": "t3", "name": "Nucleic Acids"}]}
                        ]
                    },
                    {
                        "id": "maths",
                        "name": "Mathematics",
                        "chapters": [
                            {"id": "ch1", "name": "Relations and Functions", "topics": [{"id": "t1", "name": "Types of Relations"}, {"id": "t2", "name": "One-one and Onto Functions"}, {"id": "t3", "name": "Inverse Functions"}]},
                            {"id": "ch2", "name": "Inverse Trigonometric Functions", "topics": [{"id": "t1", "name": "Principal Value Branch"}, {"id": "t2", "name": "Properties"}]},
                            {"id": "ch3", "name": "Matrices", "topics": [{"id": "t1", "name": "Operations on Matrices"}, {"id": "t2", "name": "Transpose and Inverse"}]},
                            {"id": "ch4", "name": "Determinants", "topics": [{"id": "t1", "name": "Properties"}, {"id": "t2", "name": "Area of Triangle"}, {"id": "t3", "name": "Solving System of Equations"}]},
                            {"id": "ch5", "name": "Continuity and Differentiability", "topics": [{"id": "t1", "name": "Continuity"}, {"id": "t2", "name": "Chain Rule"}, {"id": "t3", "name": "Mean Value Theorem"}]},
                            {"id": "ch6", "name": "Application of Derivatives", "topics": [{"id": "t1", "name": "Rate of Change"}, {"id": "t2", "name": "Increasing/Decreasing Functions"}, {"id": "t3", "name": "Maxima and Minima"}]},
                            {"id": "ch7", "name": "Integrals", "topics": [{"id": "t1", "name": "Indefinite Integrals"}, {"id": "t2", "name": "Definite Integrals"}, {"id": "t3", "name": "Properties of Definite Integrals"}]},
                            {"id": "ch8", "name": "Application of Integrals", "topics": [{"id": "t1", "name": "Area under Simple Curves"}]},
                            {"id": "ch9", "name": "Differential Equations", "topics": [{"id": "t1", "name": "Order and Degree"}, {"id": "t2", "name": "General and Particular Solutions"}, {"id": "t3", "name": "Linear Differential Equations"}]},
                            {"id": "ch10", "name": "Vector Algebra", "topics": [{"id": "t1", "name": "Dot Product"}, {"id": "t2", "name": "Cross Product"}]},
                            {"id": "ch11", "name": "Three Dimensional Geometry", "topics": [{"id": "t1", "name": "Direction Cosines"}, {"id": "t2", "name": "Equation of Line"}, {"id": "t3", "name": "Equation of Plane"}]},
                            {"id": "ch12", "name": "Linear Programming", "topics": [{"id": "t1", "name": "Objective Function"}, {"id": "t2", "name": "Graphical Solution"}]},
                            {"id": "ch13", "name": "Probability", "topics": [{"id": "t1", "name": "Conditional Probability"}, {"id": "t2", "name": "Bayes' Theorem"}]}
                        ]
                    }
                ]
            }
        ]
    }
    
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=2)
    print("Full dataset created successfully.")

if __name__ == "__main__":
    create_full_data()
