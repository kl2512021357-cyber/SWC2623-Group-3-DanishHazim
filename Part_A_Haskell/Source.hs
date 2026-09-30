import Text.Printf (printf)

-- SWC2623 Software Development Paradigms
-- Coursework 2
-- Part A: Functional Programming (Haskell)
-- Learning Performance Analysis

type Learner = (String, String, [Double])

learners :: [Learner]
learners =
    [ ("L001", "Aina",  [85, 90, 88])
    , ("L002", "Amir",  [75, 80, 85])
    , ("L003", "Siti",  [80, 80, 80])
    , ("L004", "Faris", [92, 88, 90])
    , ("L005", "Nadia", [92, 88, 90])
    ]

-- Pure function to calculate average score
averageScore :: Learner -> Double
averageScore (_, _, scores) =
    sum scores / fromIntegral (length scores)

-- Get learner ID
learnerID :: Learner -> String
learnerID (lid, _, _) = lid

-- Get learner name
learnerName :: Learner -> String
learnerName (_, name, _) = name

-- Find learners with average score 80 or above
highAchievers :: [Learner] -> [Learner]
highAchievers =
    filter (\learner -> averageScore learner >= 80)

-- Find top-performing learner
-- Tie rule:
-- If two learners have the same highest average,
-- the learner appearing first in the list is selected.
topLearner :: [Learner] -> Learner
topLearner [] =
    error "Learner list cannot be empty."

topLearner [x] = x

topLearner (x:xs)
    | averageScore x >= averageScore best = x
    | otherwise = best
    where
        best = topLearner xs

-- Display learner information with 2 decimal places
displayLearner :: Learner -> String
displayLearner learner =
    learnerID learner
    ++ " - "
    ++ learnerName learner
    ++ " | Average: "
    ++ printf "%.2f" (averageScore learner)

main :: IO ()
main = do
    putStrLn "=========================================="
    putStrLn " SMART LEARNING PERFORMANCE ANALYSIS"
    putStrLn "=========================================="

    putStrLn "\nAll Learners:"
    mapM_ (putStrLn . displayLearner) learners

    putStrLn "\nHigh Achievers (Average >= 80):"
    mapM_ (putStrLn . displayLearner) (highAchievers learners)

    putStrLn "\nTop Performing Learner:"
    putStrLn (displayLearner (topLearner learners))

    putStrLn "\n=========================================="
    putStrLn " TEST CASES"
    putStrLn "=========================================="

    -- Test 1: Normal case
    let normalTest =
            ("T001", "Normal Learner", [70, 75, 80])

    putStrLn "\nTest 1 - Normal Case:"
    putStrLn (displayLearner normalTest)

    -- Test 2: Boundary case
    let boundaryTest =
            ("T002", "Boundary Learner", [80, 80, 80])

    putStrLn "\nTest 2 - Boundary Case (Average = 80):"
    putStrLn (displayLearner boundaryTest)

    putStrLn "High Achiever:"
    print (averageScore boundaryTest >= 80)

    -- Test 3: Tie case
    let tieTest =
            [ ("T003", "Learner A", [90, 90, 90])
            , ("T004", "Learner B", [90, 90, 90])
            ]

    putStrLn "\nTest 3 - Tie Case:"
    mapM_ (putStrLn . displayLearner) tieTest

    putStrLn "Selected Top Learner:"
    putStrLn (displayLearner (topLearner tieTest))

    putStrLn "\nTie Rule: First learner in the list is selected."
    putStrLn "\nPYTHON_DATA"

    mapM_
        (\learner ->
            putStrLn (
                learnerID learner
                ++ "|"
                ++ learnerName learner
                ++ "|"
                ++ show (averageScore learner)
            )
        )
        learners
        
    putStrLn "\n=========================================="
    putStrLn " END OF PROGRAM"
    putStrLn "=========================================="