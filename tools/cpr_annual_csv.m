function [] = cpr_annual_csv(year, daysInYear, irrType, ulocs)

lat_lon_pairs = csvread('SolarAnywhere_Lat_Lon.csv');
s1 = 'DOY';
for coord = 1:ulocs
    row = [];
    res = [];
    lat = lat_lon_pairs(coord, 1);
    lon = lat_lon_pairs(coord, 2);
    loc_str = strcat('N', num2str(lat), 'W', num2str(abs(lon)));
    variable = load(strcat(loc_str, '.mat'));
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