% SWC2623 Software Development Paradigms
% Coursework 2
% Part B: Logic Programming (Prolog)
% Module Advisory and Certification


% ==========================================================
% 1. LEARNERS
% ==========================================================

learner(l001, aina).
learner(l002, amir).
learner(l003, siti).
learner(l004, faris).
learner(l005, nadia).


% ==========================================================
% 2. MODULES
% ==========================================================

module(programming_fundamentals).
module(database_systems).
module(web_development).
module(data_structures).
module(software_engineering).
module(final_project).


% ==========================================================
% 3. COMPLETED MODULES
% ==========================================================

completed(l001, programming_fundamentals).
completed(l001, database_systems).

completed(l002, programming_fundamentals).

completed(l003, programming_fundamentals).
completed(l003, database_systems).

completed(l004, programming_fundamentals).
completed(l004, database_systems).
completed(l004, web_development).
completed(l004, data_structures).
completed(l004, software_engineering).
completed(l004, final_project).

completed(l005, programming_fundamentals).
completed(l005, web_development).


% ==========================================================
% 4. PREREQUISITES
% ==========================================================

prerequisite(database_systems, programming_fundamentals).
prerequisite(web_development, programming_fundamentals).
prerequisite(data_structures, programming_fundamentals).
prerequisite(software_engineering, database_systems).
prerequisite(software_engineering, data_structures).
prerequisite(final_project, software_engineering).


% ==========================================================
% 5. PROGRAMME REQUIRED MODULES
% ==========================================================

required_module(programming_fundamentals).
required_module(database_systems).
required_module(web_development).
required_module(data_structures).
required_module(software_engineering).
required_module(final_project).


% ==========================================================
% 6. ELIGIBILITY RULE
% ==========================================================

% A learner is eligible if:
% 1. The module exists
% 2. The learner has not completed it
% 3. All prerequisites have been completed

eligible(Learner, Module) :-
    learner(Learner, _),
    module(Module),
    \+ completed(Learner, Module),
    forall(
        prerequisite(Module, Required),
        completed(Learner, Required)
    ).


% ==========================================================
% 7. RECOMMENDATION RULE
% ==========================================================

recommend_module(Learner, Module) :-
    eligible(Learner, Module).


% ==========================================================
% 8. CERTIFICATION RULE
% ==========================================================

eligible_for_certification(Learner) :-
    learner(Learner, _),
    forall(
        required_module(Module),
        completed(Learner, Module)
    ).