public class Temp {
    public static void main(String[] args) {
        String[] testDates = {"2/12/2002", "2-12/2002", "02/12-2002","02/1/2002"};
        
        for (String date : testDates) {
            System.out.println("Input: " + date + " -> Formatted Date: " + formatDate(date));
        }
    }

    public static String formatDate(String date) {
        // Normalize delimiters by replacing '-' with '/'
        String normalizedDate = date.replace('-', '/');

        // Split the date parts
        String[] dateParts = normalizedDate.split("/");

        // Ensure we have exactly 3 parts: day, month, and year
        if (dateParts.length != 3) {
            return "Invalid date format.";
        }

        // Extract day, month, and year
        String day = dateParts[0].trim();
        String month = dateParts[1].trim();
        String year = dateParts[2].trim();

        // Format day and month to be two digits
        StringBuilder formattedDate = new StringBuilder();
        formattedDate.append(formatTwoDigit(day)).append('/');
        formattedDate.append(formatTwoDigit(month)).append('/');
        formattedDate.append(year);

        return formattedDate.toString();
    }

    private static String formatTwoDigit(String value) {
        // If the value is a single digit, add a leading zero
        if (value.length() == 1) {
            return "0" + value;
        }
        return value;
    }
}
