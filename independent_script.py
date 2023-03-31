import traceback


def independent_calculate_attendance_and_missing(days):
    try:
        maximum_miss_consecutive_days = 4  # As per in question its static

        # Validation for the passed days
        if days < maximum_miss_consecutive_days or days < 0:
            raise ValueError("Invalid inputs which should be above 4 days")

        # With a new variable store 2d list
        listing_data = [[0] * (maximum_miss_consecutive_days + 1) for _ in range(days + 1)]

        # The base tables should be filled up
        for i in range(maximum_miss_consecutive_days):
            listing_data[0][i] = 1

        # Compute the dynamic programming table using bottom-up approach
        for i in range(1, days + 1):
            for j in range(maximum_miss_consecutive_days - 1, -1, -1):
                listing_data[i][j] = listing_data[i - 1][0] + listing_data[i - 1][j + 1]

        total_ways_to_attend_days = listing_data[days][0]
        total_ways_to_miss_day = listing_data[days-1][1]

        # result has been added as per the asked logic in the question
        result = f"{total_ways_to_miss_day}/{total_ways_to_attend_days}"
        return result
    except Exception as e:
        traceback.format_exc()
        print("Check the error for exception {} ".format(str(e)))
        return None


take_days = int(input("Enter the no of days "))
final_result = {"No of days is": take_days, "Probability of missing days": f"{independent_calculate_attendance_and_missing(take_days)}"}
print(final_result)
print("Probability of missing days is", independent_calculate_attendance_and_missing(take_days))
