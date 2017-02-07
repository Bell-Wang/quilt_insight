function [] = cpr_annual_csv(year, daysInYear, irrType, ulocs)

% These are the list of locations where data exists
lat_lon_pairs = csvread('SolarAnywhere_Lat_Lon.csv');
% String used to programatically access the day of year from .mat files
s1 = 'DOY';
% Number of unique locations in the dataset
for coord = 1:ulocs
    % Placeholder for the row to be added
    row = [];
    % Placeholder the the result that will be returned
    res = [];
    % Grab the location from the from the strings in
    % 'SolarAnywhere_Lat_Lon.csv'
    lat = lat_lon_pairs(coord, 1);
    lon = lat_lon_pairs(coord, 2);
    % Build the location string
    loc_str = strcat('N', num2str(lat), 'W', num2str(abs(lon)));
    % Load the .mat file into variable 
    variable = load(strcat(loc_str, '.mat'));
    % Build a year string to access tables
    yr_str = strcat('Y', num2str(year));
    for hour = 1:48
        for day = 1:daysInYear
            row = [row, rot90(rot90(variable.(loc_str).(yr_str).(strcat(s1, num2str(day))).(irrType)(:,:,hour)))];
        end
        res = [res;row];
        row = [];
    end
    csvwrite(strcat('csv/',loc_str,'_',num2str(year),'_',irrType,'.csv'),res);
end
end